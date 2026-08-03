from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from utils.db_connection import get_db


habit_bp = Blueprint("habit", __name__)


# ==============================
# View Habits Page
# ==============================

@habit_bp.route("/habits")
@login_required
def habits():

    db = get_db()
    cursor = db.connection.cursor()

    user_id = current_user.id

    cursor.execute(
        """
        SELECT * FROM habits
        WHERE user_id = %s
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    habits = cursor.fetchall()

    return render_template(
        "habits.html",
        habits=habits
    )


# ==============================
# Create New Habit
# ==============================

@habit_bp.route("/create_habit", methods=["POST"])
@login_required
def create_habit():

    habit_name = request.form.get("habit_name")
    category = request.form.get("category")
    difficulty = request.form.get("difficulty")

    db = get_db()
    cursor = db.connection.cursor()

    user_id = current_user.id

    cursor.execute(
        """
        INSERT INTO habits (user_id, habit_name, category, difficulty)
        VALUES (%s, %s, %s, %s)
        """,
        (user_id, habit_name, category, difficulty)
    )

    db.connection.commit()

    flash("Habit created successfully.")

    return redirect(url_for("habit.habits"))