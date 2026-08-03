def calculate_productivity_score(logs):

    if not logs:
        return 0, "Start logging study sessions."

    total_focus = 0
    total_quiz = 0
    total_time = 0
    total_skipped = 0

    count = len(logs)

    for log in logs:

        total_focus += log["focus"]
        total_quiz += log["quiz_score"]
        total_time += log["study_time"]
        total_skipped += log["skipped_days"]

    avg_focus = total_focus / count
    avg_quiz = total_quiz / count
    avg_time = total_time / count
    avg_skipped = total_skipped / count

    # score formula
    score = (
        (avg_focus * 10) +
        (avg_quiz * 0.4) +
        (avg_time * 0.2) -
        (avg_skipped * 5)
    )

    score = max(0, min(100, int(score)))

    # AI message
    if score >= 80:
        message = "Highly Productive Learner 🚀"
    elif score >= 60:
        message = "Consistent Learner 📚"
    elif score >= 40:
        message = "Moderate Productivity ⚡"
    else:
        message = "Needs Better Study Consistency"

    return score, message