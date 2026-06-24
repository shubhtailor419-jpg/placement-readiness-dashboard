import pandas as pd
import random

rows = []

for i in range(1, 1001):

    cgpa = round(random.uniform(5.0, 10.0), 2)
    python_score = random.randint(35, 100)
    communication = random.randint(35, 100)
    sql = random.randint(35, 100)
    projects = random.randint(0, 6)
    internship = random.randint(0, 1)

    score = (
        cgpa * 8
        + python_score * 0.25
        + communication * 0.20
        + sql * 0.20
        + projects * 3
        + internship * 10
    )

    placement = 1 if score > 95 else 0

    rows.append(
        [
            i,
            cgpa,
            python_score,
            communication,
            sql,
            projects,
            internship,
            placement
        ]
    )

df = pd.DataFrame(
    rows,
    columns=[
        "Student_ID",
        "CGPA",
        "Python",
        "Communication",
        "SQL",
        "Projects",
        "Internship",
        "Placement"
    ]
)

import os

os.makedirs("data", exist_ok=True)

df.to_csv(
    "data/placement_dataset.csv",
    index=False
)

print("Dataset Created")