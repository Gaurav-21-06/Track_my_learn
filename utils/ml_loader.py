import joblib
from config import Config


prediction_model = None
recommendation_model = None


def load_models():
    global prediction_model
    global recommendation_model

    try:
        prediction_model = joblib.load(Config.PREDICTION_MODEL_PATH)
    except Exception:
        prediction_model = None

    try:
        recommendation_model = joblib.load(Config.RECOMMENDATION_MODEL_PATH)
    except Exception:
        recommendation_model = None


def get_prediction_model():
    return prediction_model


def get_recommendation_model():
    return recommendation_model