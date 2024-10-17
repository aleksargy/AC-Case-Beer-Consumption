import pandas as pd
import numpy as np
from datetime import timedelta

np.random.seed(42)

num_students = 100
num_events = 30
num_days = 30

# Ranges for GPA, happiness, sleep, and social life scores
gpa_range = (2.0, 4.0)
happiness_range = (1, 10)
sleep_hours_range = (4, 10)
social_life_range = (1, 10)
beer_consumption_range = (0, 10)

# Students dataset
students_data = []
for i in range(1, num_students + 1):
    age = np.random.randint(18, 25)
    gender = np.random.choice(["Male", "Female"])
    major = np.random.choice(
        ["Engineering", "Science", "Arts", "Business", "Social Sciences"]
    )
    gpa = np.random.uniform(*gpa_range)
    credits_completed = np.random.randint(30, 120)
    students_data.append([f"S{i:03}", age, gender, major, gpa, credits_completed])

students_df = pd.DataFrame(
    students_data,
    columns=["student_id", "age", "gender", "major", "GPA", "credits_completed"],
)

# Beer consumption dataset
dates = pd.date_range(end=pd.Timestamp.today(), periods=num_days).to_list()
beer_consumption_data = []
for student_id in students_df["student_id"]:
    for date in dates:
        beers_consumed = np.random.poisson(
            2
        )  # Assume average of 2 beers/day with some variation
        beer_consumption_data.append([student_id, date, beers_consumed])

beer_consumption_df = pd.DataFrame(
    beer_consumption_data, columns=["student_id", "date", "beers_consumed"]
)

# Well-being dataset
well_being_data = []
for student_id in students_df["student_id"]:
    total_beer_consumed = beer_consumption_df.loc[
        beer_consumption_df["student_id"] == student_id, "beers_consumed"
    ].sum()
    # Assume that higher beer consumption correlates negatively with sleep and GPA but positively with social life
    happiness_score = np.random.uniform(*happiness_range) - (total_beer_consumed * 0.05)
    sleep_hours = np.random.uniform(*sleep_hours_range) - (total_beer_consumed * 0.05)
    social_life_score = np.random.uniform(*social_life_range) + (
        total_beer_consumed * 0.05
    )
    well_being_data.append(
        [student_id, happiness_score, sleep_hours, social_life_score]
    )

well_being_df = pd.DataFrame(
    well_being_data,
    columns=["student_id", "happiness_score", "sleep_hours", "social_life_score"],
)

# Events dataset
event_types = ["Party", "Study Group", "Sports Event"]
events_data = []
for i in range(1, num_events + 1):
    event_date = np.random.choice(dates)
    event_type = np.random.choice(event_types)
    average_beer_consumed = np.random.uniform(
        2, 10
    )  # Assume an average of 2-10 beers consumed at events
    events_data.append([f"E{i:03}", event_date, event_type, average_beer_consumed])

events_df = pd.DataFrame(
    events_data,
    columns=["event_id", "event_date", "event_type", "average_beer_consumed"],
)

# Save the datasets to CSV files
students_df.to_csv("data/students.csv", index=False)
beer_consumption_df.to_csv("data/beer_consumption.csv", index=False)
well_being_df.to_csv("data/well_being.csv", index=False)
events_df.to_csv("data/events.csv", index=False)
