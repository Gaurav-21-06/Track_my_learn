from flask import Blueprint, render_template
from flask_login import login_required, current_user
import numpy as np

from utils.db_connection import get_db
from utils.ml_loader import recommendation_model


recommendation_bp = Blueprint("recommendation", __name__)


# ==============================
# Recommendation Page
# ==============================

@recommendation_bp.route("/recommendations")
@login_required
def recommendations():

    db = get_db()
    cursor = db.connection.cursor()

    user_id = current_user.id

    cursor.execute(
        """
        SELECT study_time, skipped_days, quiz_score, mood, focus
        FROM study_logs
        WHERE user_id = %s
        ORDER BY created_at DESC
        LIMIT 20
        """,
        (user_id,)
    )

    logs = cursor.fetchall()

    predicted_time = None
    message = None

    if logs:

        data = []

        for log in logs:
            data.append([
                log["study_time"],
                log["skipped_days"],
                log["quiz_score"],
                log["mood"],
                log["focus"]
            ])

        data = np.array(data)

        # Try ML recommendation first
        try:

            if recommendation_model:

                predicted_time = int(
                    recommendation_model.predict(data).mean()
                )

        except:
            predicted_time = None


        # If ML fails → fallback recommendation
        if predicted_time is None:

            avg_time = sum([log["study_time"] for log in logs]) / len(logs)

            predicted_time = int(avg_time)

        message = f"Based on your study behavior, studying around {predicted_time} minutes per session may improve productivity."

    return render_template(
        "recommendations.html",
        predicted_time=predicted_time,
        message=message
    )