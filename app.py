from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_mysqldb import MySQL

from config import Config
from utils.ml_loader import load_models
from utils.db_connection import init_db
from models.user_model import User


# Import route modules
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.habit_routes import habit_bp
from routes.studylog_routes import studylog_bp
from routes.timer_routes import timer_bp
from routes.insights_routes import insights_bp
from routes.prediction_routes import prediction_bp
from routes.history_routes import history_bp
from routes.recommendation_routes import recommendation_bp


app = Flask(__name__)
app.config.from_object(Config)


# ==============================
# Initialize Extensions
# ==============================

mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth.signin"


# ==============================
# Initialize Database Utility
# ==============================

init_db(app)


# ==============================
# Load ML Models
# ==============================

load_models()

# ==============================
# Flask Login User Loader
# ==============================

from utils.db_connection import get_db
from models.user_model import User

@login_manager.user_loader
def load_user(user_id):

    db = get_db()
    cursor = db.connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )

    user = cursor.fetchone()

    if user:
        return User(user)

    return None


# ==============================
# Register Blueprints
# ==============================

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(habit_bp)
app.register_blueprint(studylog_bp)
app.register_blueprint(timer_bp)
app.register_blueprint(insights_bp)
app.register_blueprint(prediction_bp)
app.register_blueprint(history_bp)
app.register_blueprint(recommendation_bp)


# ==============================
# Run Application
# ==============================

if __name__ == "__main__":
    app.run(debug=True)