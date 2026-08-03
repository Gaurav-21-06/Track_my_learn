import numpy as np
from sklearn.cluster import KMeans


# ==============================
# Pattern Analysis using K-Means
# ==============================

def analyze_patterns(logs):

    if len(logs) < 3:
        return None

    data = np.array([[l["study_time"], l["focus"], l["mood"]] for l in logs])

    kmeans = KMeans(n_clusters=2, random_state=42)

    clusters = kmeans.fit_predict(data)

    return clusters


# ==============================
# AI Insight Message Generator
# ==============================

def generate_insight_message(avg_focus, best_category, total_sessions):

    message_parts = []

    # Focus analysis
    if avg_focus >= 4:
        message_parts.append(
            "You maintain excellent focus during your study sessions."
        )

    elif avg_focus >= 3:
        message_parts.append(
            "Your focus level is moderate. Try minimizing distractions to improve productivity."
        )

    else:
        message_parts.append(
            "Your focus level appears low. Consider shorter sessions and a better study environment."
        )

    # Category analysis
    message_parts.append(
        f"You spend most of your study time on {best_category}."
    )

    # Study consistency
    if total_sessions >= 20:
        message_parts.append(
            "You have a strong study consistency. Keep maintaining your learning streak."
        )

    elif total_sessions >= 10:
        message_parts.append(
            "You are developing a consistent study habit. Logging more sessions will improve AI analysis."
        )

    else:
        message_parts.append(
            "Start logging more study sessions so the AI can understand your learning behavior better."
        )

    return " ".join(message_parts)