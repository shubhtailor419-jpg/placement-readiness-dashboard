def calculate_readiness_score(
    cgpa,
    python_score,
    communication,
    sql,
    projects,
    internship
):

    score = (
        cgpa * 10
        + python_score
        + communication
        + sql
        + projects * 10
        + internship * 20
    ) / 5

    return round(score, 2)


def generate_recommendations(
    cgpa,
    python_score,
    communication,
    sql,
    projects,
    internship
):

    recommendations = []

    if cgpa < 7.5:
        recommendations.append(
            "Improve academic performance."
        )

    if python_score < 75:
        recommendations.append(
            "Strengthen Python skills."
        )

    if communication < 75:
        recommendations.append(
            "Improve communication skills."
        )

    if sql < 70:
        recommendations.append(
            "Practice SQL regularly."
        )

    if projects < 3:
        recommendations.append(
            "Build more projects."
        )

    if internship == 0:
        recommendations.append(
            "Apply for internships."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "You are placement ready."
        )

    return recommendations