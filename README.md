# Placement Readiness Dashboard

A Streamlit app to predict student placement readiness and provide skill recommendations.

## Features

- Placement prediction using machine learning
- Student readiness score calculation
- Skill gap analysis and recommendations
- Analytics dashboard for placement statistics
- Individual student performance insights

## Installation

```bash
git clone https://github.com/yourusername/placement-readiness-dashboard.git
cd placement-readiness-dashboard
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

## Project Structure

```
placement-readiness-dashboard/
├── app.py                 # Main application
├── requirements.txt       # Dependencies
└── README.md             # This file
```

## How It Works

1. **Placement Prediction** - Predicts if a student will be placed
2. **Readiness Score** - Calculates overall placement readiness
3. **Skill Recommendations** - Suggests skills to improve
4. **Analytics** - Shows placement statistics and trends

## Model

- Algorithm: Random Forest
- Predicts: Student placement success
- Based on: Academic scores, skills, experience

## Dataset

The app works with student data including:
- GPA and test scores
- Technical skills
- Projects and internship experience
- Communication abilities

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Open browser to http://localhost:8501
```

## Notes

- Ensure you have a CSV file with student data
- Place data in the `data/` folder
- The model requires historical placement data for training
