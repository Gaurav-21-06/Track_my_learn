import pandas as pd
import random
import os
import sys

# Allow access to parent directory (to import config)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import Config


categories = ["programming", "mathematics", "reading", "science", "language", "other"]
difficulties = ["easy", "medium", "hard"]


def generate_prediction_dataset(rows=1000):

    data = []

    for _ in range(rows):

        category = random.choice(categories)
        difficulty = random.choice(difficulties)

        study_time = random.randint(10, 120)
        skipped_days = random.randint(0, 5)
        quiz_score = random.randint(40, 100)

        mood = random.randint(1, 5)
        focus = random.randint(1, 5)

        score_factor = (focus + mood) / 2
        skip_factor = skipped_days

        if score_factor >= 3 and skip_factor <= 2:
            completed = 1
        else:
            completed = 0

        data.append([
            category,
            difficulty,
            study_time,
            skipped_days,
            quiz_score,
            mood,
            focus,
            completed
        ])

    columns = [
        "category",
        "difficulty",
        "study_time",
        "skipped_days",
        "quiz_score",
        "mood",
        "focus",
        "completed"
    ]

    df = pd.DataFrame(data, columns=columns)

    os.makedirs(os.path.dirname(Config.PREDICTION_DATASET_PATH), exist_ok=True)
    df.to_csv(Config.PREDICTION_DATASET_PATH, index=False)

    print("Prediction dataset generated successfully.")


def generate_recommendation_dataset(rows=1000):

    data = []

    for _ in range(rows):

        category = random.choice(categories)
        difficulty = random.choice(difficulties)

        mood = random.randint(1, 5)
        focus = random.randint(1, 5)
        quiz_score = random.randint(40, 100)

        base_time = 30

        if difficulty == "medium":
            base_time += 10

        if difficulty == "hard":
            base_time += 20

        base_time += focus * 2
        base_time += mood * 2

        recommended_time = base_time

        data.append([
            category,
            difficulty,
            focus,
            mood,
            quiz_score,
            recommended_time
        ])

    columns = [
        "category",
        "difficulty",
        "focus",
        "mood",
        "quiz_score",
        "recommended_time"
    ]

    df = pd.DataFrame(data, columns=columns)

    os.makedirs(os.path.dirname(Config.RECOMMENDATION_DATASET_PATH), exist_ok=True)
    df.to_csv(Config.RECOMMENDATION_DATASET_PATH, index=False)

    print("Recommendation dataset generated successfully.")


if __name__ == "__main__":

    generate_prediction_dataset(1000)
    generate_recommendation_dataset(1000)