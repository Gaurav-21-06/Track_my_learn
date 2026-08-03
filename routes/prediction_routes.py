from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import joblib

from utils.db_connection import get_db
from config import Config


prediction_bp = Blueprint("prediction", __name__)


# ==============================
# Load Prediction Model
# ==============================

prediction_model = joblib.load(Config.PREDICTION_MODEL_PATH)


# ==============================
# Prediction Page
# ==============================

@prediction_bp.route("/prediction", methods=["GET", "POST"])
@login_required
def prediction():

    db = get_db()
    cursor = db.connection.cursor()

    user_id = current_user.id

    # ==============================
    # Fetch Habits for Dropdown
    # ==============================

    cursor.execute(
        "SELECT id, habit_name FROM habits WHERE user_id = %s",
        (user_id,)
    )

    habits = cursor.fetchall()

    prediction_result = None
    confidence = None

    # ==============================
    # Handle Prediction Request
    # ==============================

    if request.method == "POST":

        study_time = int(request.form.get("study_time"))
        skipped_days = int(request.form.get("skipped_days"))
        quiz_score = int(request.form.get("quiz_score"))
        mood = int(request.form.get("mood"))
        focus = int(request.form.get("focus"))

        # Add 2 placeholder features (for model compatibility)
        difficulty = 2
        category = 3

        features = [[
            study_time,
            skipped_days,
            quiz_score,
            mood,
            focus,
            difficulty,
            category
        ]]

        # Run prediction
        pred = prediction_model.predict(features)[0]
        prob = prediction_model.predict_proba(features)[0]

        prediction_result = "Completed" if pred == 1 else "Skipped"
        confidence = round(max(prob) * 100, 2)

        # ==============================
        # Save Prediction History
        # ==============================
        habit_id = request.form.get("habit_id")

        cursor.execute(
            """
            INSERT INTO prediction_history
            (user_id, habit_id, prediction_result, confidence)
            VALUES (%s, %s, %s, %s)
            """,
            (user_id, habit_id, prediction_result, confidence)
        )

        db.connection.commit()

    return render_template(
        "prediction.html",
        habits=habits,
        prediction_result=prediction_result,
        confidence=confidence
    )