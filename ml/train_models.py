import pandas as pd
import os
import sys
import joblib

# Allow access to parent directory (to import config)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import Config

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression


def train_prediction_model():

    df = pd.read_csv(Config.PREDICTION_DATASET_PATH)

    label_encoders = {}

    for column in ["category", "difficulty"]:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

    X = df.drop("completed", axis=1)
    y = df["completed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=200, random_state=42)

    model.fit(X_train, y_train)

    os.makedirs(os.path.dirname(Config.PREDICTION_MODEL_PATH), exist_ok=True)

    joblib.dump(model, Config.PREDICTION_MODEL_PATH)

    print("Prediction model trained and saved.")


def train_recommendation_model():

    df = pd.read_csv(Config.RECOMMENDATION_DATASET_PATH)

    label_encoders = {}

    for column in ["category", "difficulty"]:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

    X = df.drop("recommended_time", axis=1)
    y = df["recommended_time"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    os.makedirs(os.path.dirname(Config.RECOMMENDATION_MODEL_PATH), exist_ok=True)

    joblib.dump(model, Config.RECOMMENDATION_MODEL_PATH)

    print("Recommendation model trained and saved.")


if __name__ == "__main__":

    train_prediction_model()

    train_recommendation_model()