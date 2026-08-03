from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from utils.db_connection import get_db


timer_bp = Blueprint("timer", __name__)


# ==============================
# Timer Page
# ==============================

@timer_bp.route("/timer")
@login_required
def timer():

    db = get_db()
    cursor = db.connection.cursor()

    user_id = current_user.id

    # Load habits for dropdown
    cursor.execute(
        """
        SELECT * FROM habits
        WHERE user_id = %s
        """,
        (user_id,)
    )

    habits = cursor.fetchall()

    # Load timer logs
    cursor.execute(
        """
        SELECT timer_logs.*, habits.habit_name
        FROM timer_logs
        JOIN habits ON timer_logs.habit_id = habits.id
        WHERE timer_logs.user_id = %s
        ORDER BY timer_logs.created_at DESC
        """,
        (user_id,)
    )

    timers = cursor.fetchall()

    return render_template(
        "timer.html",
        habits=habits,
        timers=timers
    )


# ==============================
# Save Timer Session
# ==============================

@timer_bp.route("/save_timer", methods=["POST"])
@login_required
def save_timer():

    habit_id = request.form.get("habit_id")
    duration_seconds = request.form.get("duration_seconds")

    db = get_db()
    cursor = db.connection.cursor()

    user_id = current_user.id

    cursor.execute(
        """
        INSERT INTO timer_logs (user_id, habit_id, duration_seconds)
        VALUES (%s, %s, %s)
        """,
        (user_id, habit_id, duration_seconds)
    )

    db.connection.commit()

    flash("Timer session saved.")

    return redirect(url_for("timer.timer"))


# ==============================
# Reset Timer Logs
# ==============================

@timer_bp.route("/reset_timer")
@login_required
def reset_timer():

    db = get_db()
    cursor = db.connection.cursor()

    user_id = current_user.id

    cursor.execute(
        """
        DELETE FROM timer_logs
        WHERE user_id = %s
        """,
        (user_id,)
    )

    db.connection.commit()

    flash("Timer sessions cleared.")

    return redirect(url_for("timer.timer"))