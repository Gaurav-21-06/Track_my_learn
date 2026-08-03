from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from utils.db_connection import get_db
from config import Config

import csv


studylog_bp = Blueprint("studylog", __name__)


# ==============================
# Study Log Page
# ==============================

@studylog_bp.route("/studylog")
@login_required
def studylog():

    db = get_db()
    cursor = db.connection.cursor()

    user_id = current_user.id

    # Get habits for dropdown
    cursor.execute(
        """
        SELECT * FROM habits
        WHERE user_id = %s
        """,
        (user_id,)
    )

    habits = cursor.fetchall()

    # Get recent logs
    cursor.execute(
        """
        SELECT study_logs.*, habits.habit_name
        FROM study_logs
        JOIN habits ON study_logs.habit_id = habits.id
        WHERE study_logs.user_id = %s
        ORDER BY study_logs.created_at DESC
        LIMIT 10
        """,
        (user_id,)
    )

    logs = cursor.fetchall()

    return render_template(
        "studylog.html",
        habits=habits,
        logs=logs
    )


# ==============================
# Save Study Log
# ==============================

@studylog_bp.route("/save_studylog", methods=["POST"])
@login_required
def save_studylog():

    habit_id = request.form.get("habit_id")
    study_time = int(request.form.get("study_time"))
    skipped_days = int(request.form.get("skipped_days"))
    quiz_score = int(request.form.get("quiz_score"))
    mood = int(request.form.get("mood"))
    focus = int(request.form.get("focus"))

    completed = request.form.get("completed")

    if completed == "on":
        completed = True
    else:
        completed = False

    db = get_db()
    cursor = db.connection.cursor()

    user_id = current_user.id

    # ==============================
    # Insert Study Log into Database
    # ==============================

    cursor.execute(
        """
        INSERT INTO study_logs
        (user_id, habit_id, study_time, skipped_days, quiz_score, mood, focus, completed)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (user_id, habit_id, study_time, skipped_days, quiz_score, mood, focus, completed)
    )

    db.connection.commit()

    # ==============================
    # Append Data to ML Dataset
    # ==============================

    try:

        with open(Config.PREDICTION_DATASET_PATH, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                study_time,
                skipped_days,
                quiz_score,
                mood,
                focus,
                1 if completed else 0
            ])

    except Exception as e:
        print("Dataset append error:", e)

    flash("Study log saved successfully.")

    return redirect(url_for("studylog.studylog"))