from flask import Blueprint, render_template
from flask_login import login_required, current_user
from utils.db_connection import get_db


history_bp = Blueprint("history", __name__)


# ==============================
# Prediction History Page
# ==============================

@history_bp.route("/history")
@login_required
def history():

    db = get_db()
    cursor = db.connection.cursor()

    user_id = current_user.id

    cursor.execute(
    """
    SELECT
        prediction_history.prediction_result,
        prediction_history.confidence,
        prediction_history.created_at,
        habits.habit_name
    FROM prediction_history
    JOIN habits
    ON prediction_history.habit_id = habits.id
    WHERE prediction_history.user_id = %s
    ORDER BY prediction_history.created_at DESC
    """,
    (user_id,)
)

    history = cursor.fetchall()

    return render_template(
        "history.html",
        history=history
    )