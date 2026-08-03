import os

class Config:
    
    # Flask Secret Key
    SECRET_KEY = "trackmylearn_ai_secret_key"

    # ==============================
    # MySQL Database Configuration
    # ==============================

    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "trackmylearn_ai"
    MYSQL_CURSORCLASS = "DictCursor"

    # ==============================
    # Email Configuration
    # ==============================

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # Replace this with your Gmail
    MAIL_USERNAME = "your_email@gmail.com"

    # Replace this with Gmail App Password
    MAIL_PASSWORD = "your_app_password"

    MAIL_DEFAULT_SENDER = "your_email@gmail.com"

    # ==============================
    # ML Model Paths
    # ==============================

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    PREDICTION_MODEL_PATH = os.path.join(
        BASE_DIR,
        "ml",
        "models",
        "prediction_model.pkl"
    )

    RECOMMENDATION_MODEL_PATH = os.path.join(
        BASE_DIR,
        "ml",
        "models",
        "recommendation_model.pkl"
    )

    # ==============================
    # Dataset Paths
    # ==============================

    PREDICTION_DATASET_PATH = os.path.join(
        BASE_DIR,
        "ml",
        "datasets",
        "prediction_dataset.csv"
    )

    RECOMMENDATION_DATASET_PATH = os.path.join(
        BASE_DIR,
        "ml",
        "datasets",
        "recommendation_dataset.csv"
    )