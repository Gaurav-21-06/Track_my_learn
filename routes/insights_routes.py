from flask import Blueprint, render_template
from flask_login import login_required, current_user
from utils.db_connection import get_db


insights_bp = Blueprint("insights", __name__)


# ==============================
# Insights Page
# ==============================

@insights_bp.route("/insights")
@login_required
def insights():

    db = get_db()
    cursor = db.connection.cursor()

    user_id = current_user.id

    # ==============================
    # Best Study Time
    # ==============================

    cursor.execute(
        """
        SELECT HOUR(created_at) AS study_hour, COUNT(*) AS total
        FROM study_logs
        WHERE user_id = %s
        GROUP BY study_hour
        ORDER BY total DESC
        LIMIT 1
        """,
        (user_id,)
    )

    best_time_data = cursor.fetchone()

    if best_time_data:
        best_study_time = f"{best_time_data['study_hour']}:00"
    else:
        best_study_time = "No data"


    # ==============================
    # Best Category
    # ==============================

    cursor.execute(
        """
        SELECT habits.category, SUM(study_logs.study_time) AS total
        FROM study_logs
        JOIN habits ON study_logs.habit_id = habits.id
        WHERE study_logs.user_id = %s
        GROUP BY habits.category
        ORDER BY total DESC
        LIMIT 1
        """,
        (user_id,)
    )

    best_category_data = cursor.fetchone()

    if best_category_data:
        best_category = best_category_data["category"]
    else:
        best_category = "No data"


    # ==============================
    # Average Focus
    # ==============================

    cursor.execute(
        """
        SELECT IFNULL(AVG(focus),0) AS avg_focus
        FROM study_logs
        WHERE user_id = %s
        """,
        (user_id,)
    )

    avg_focus = round(cursor.fetchone()["avg_focus"], 2)


    # ==============================
    # Total Sessions
    # ==============================

    cursor.execute(
        """
        SELECT COUNT(*) AS total
        FROM study_logs
        WHERE user_id = %s
        """,
        (user_id,)
    )

    total_sessions = cursor.fetchone()["total"]


    # ==============================
    # Focus Trend Data
    # ==============================

    cursor.execute(
        """
        SELECT log_date, focus
        FROM study_logs
        WHERE user_id = %s
        ORDER BY log_date ASC
        """,
        (user_id,)
    )

    trend_data = cursor.fetchall()

    trend_dates = [str(row["log_date"]) for row in trend_data]
    trend_focus = [row["focus"] for row in trend_data]


    # ==============================
    # Rule-Based AI Analysis
    # ==============================

    analysis = []

    if avg_focus < 2:
        analysis.append("Your focus level is quite low. Try shorter study sessions.")

    if avg_focus >= 2 and avg_focus < 4:
        analysis.append("Your focus is moderate. Improving consistency could boost productivity.")

    if avg_focus >= 4:
        analysis.append("You maintain strong focus during study sessions.")

    if total_sessions < 5:
        analysis.append("Not enough data yet. Continue logging your study sessions.")

    if best_category != "No data":
        analysis.append(f"You spend most time studying {best_category}.")

    if best_study_time != "No data":
        analysis.append(f"Your most productive study time appears around {best_study_time}.")


    return render_template(
        "insights.html",
        best_study_time=best_study_time,
        best_category=best_category,
        avg_focus=avg_focus,
        total_sessions=total_sessions,
        trend_dates=trend_dates,
        trend_focus=trend_focus,
        analysis=analysis
    )