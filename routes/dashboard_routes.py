from flask import Blueprint, render_template
from flask_login import login_required, current_user
from utils.db_connection import get_db
from utils.productivity_engine import calculate_productivity_score

dashboard_bp = Blueprint("dashboard", __name__)


# ==============================
# Dashboard Page
# ==============================

@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    db = get_db()
    cursor = db.connection.cursor()

    user_id = current_user.id

    # ==============================
    # Total Study Time
    # ==============================

    cursor.execute(
        """
        SELECT IFNULL(SUM(study_time),0) AS total_time
        FROM study_logs
        WHERE user_id = %s
        """,
        (user_id,)
    )

    total_time = cursor.fetchone()["total_time"]

    # ==============================
    # Completed Tasks
    # ==============================

    cursor.execute(
        """
        SELECT COUNT(*) AS completed
        FROM study_logs
        WHERE user_id = %s AND completed = TRUE
        """,
        (user_id,)
    )

    completed_tasks = cursor.fetchone()["completed"]

    # ==============================
    # Skipped Tasks
    # ==============================

    cursor.execute(
        """
        SELECT COUNT(*) AS skipped
        FROM study_logs
        WHERE user_id = %s AND completed = FALSE
        """,
        (user_id,)
    )

    skipped_tasks = cursor.fetchone()["skipped"]

    # ==============================
    # Current Streak
    # ==============================

    cursor.execute(
        """
        SELECT log_date
        FROM study_logs
        WHERE user_id = %s AND completed = TRUE
        ORDER BY log_date DESC
        """,
        (user_id,)
    )

    logs = cursor.fetchall()

    streak = 0

    if logs:
        previous_date = None

        for log in logs:

            if previous_date is None:
                streak += 1
                previous_date = log["log_date"]

            else:

                difference = (previous_date - log["log_date"]).days

                if difference == 1:
                    streak += 1
                    previous_date = log["log_date"]
                else:
                    break

    # ==============================
    # Weekly Chart Data
    # ==============================

    cursor.execute(
        """
        SELECT log_date, SUM(study_time) AS total
        FROM study_logs
        WHERE user_id = %s
        GROUP BY log_date
        ORDER BY log_date ASC
        """,
        (user_id,)
    )

    chart_data = cursor.fetchall()

    dates = [str(row["log_date"]) for row in chart_data]
    times = [row["total"] for row in chart_data]

    # ==============================
    # Pie Chart Data
    # ==============================

    pie_data = {
        "completed": completed_tasks,
        "skipped": skipped_tasks
    }

    # ==============================
    # AI Productivity Score
    # ==============================

    cursor.execute(
        """
        SELECT focus, quiz_score, study_time, skipped_days
        FROM study_logs
        WHERE user_id = %s
        """,
        (user_id,)
    )

    productivity_logs = cursor.fetchall()

    productivity_score, productivity_message = calculate_productivity_score(productivity_logs)

    # ==============================

    return render_template(
        "dashboard.html",
        total_time=total_time,
        completed_tasks=completed_tasks,
        skipped_tasks=skipped_tasks,
        streak=streak,
        chart_dates=dates,
        chart_times=times,
        pie_data=pie_data,
        productivity_score=productivity_score,
        productivity_message=productivity_message
    )