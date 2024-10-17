# Case Study: Beer Consumption and Student Well-Being

## Context:
Students across a university are consuming different amounts of beer, which may influence various aspects of their life, including academic performance, happiness, sleep patterns, and social life. The university administration is curious to understand whether beer consumption impacts these aspects and how different levels of beer consumption correlate with students’ overall well-being.

In this case study, your task is to analyse data on beer consumption, student happiness, academic grades, social engagement, and sleep quality to identify patterns and make recommendations.

## Objective:
The objective of this study is to:
1. **Determine correlations** between beer consumption and academic performance, happiness, and sleep.
2. **Explore the impact** of varying levels of beer consumption (light, moderate, heavy) on students’ well-being.
3. **Provide recommendations** for students on how to maintain a healthy balance between social drinking and academic success.

## Datasets:

1. **`students.csv`**: This dataset contains the general demographic and academic information for each student.
    - `student_id`: Unique identifier for each student.
    - `age`: The age of the student.
    - `gender`: Gender of the student.
    - `major`: The academic major of the student.
    - `GPA`: Current Grade Point Average.
    - `credits_completed`: Total number of credits the student has completed.

2. **`beer_consumption.csv`**: This dataset contains data on the students' beer consumption over the last 30 days.
    - `student_id`: Unique identifier for each student.
    - `date`: The date of beer consumption.
    - `beers_consumed`: Number of beers consumed on that day.

3. **`well_being.csv`**: This dataset tracks the well-being of students in terms of happiness, sleep quality, and social engagement.
    - `student_id`: Unique identifier for each student.
    - `happiness_score`: Self-reported happiness score on a scale of 1-10 (higher is happier).
    - `sleep_hours`: Average hours of sleep per night in the past 30 days.
    - `social_life_score`: Self-reported social engagement score on a scale of 1-10 (higher indicates more social engagement).

4. **`events.csv`**: This dataset tracks university events and social gatherings (such as parties) where beer was available.
    - `event_id`: Unique identifier for the event.
    - `event_date`: The date of the event.
    - `event_type`: Type of event (e.g., "Party", "Study Group", "Sports Event").
    - `average_beer_consumed`: Average number of beers consumed by students at the event.

## Guiding Questions:
1. **How does beer consumption correlate with academic performance (GPA)?**
   - Are students who consume more beer likely to have lower GPAs? Or does moderate consumption correlate with higher social life and happiness without affecting GPA?

2. **Is there a threshold of beer consumption that affects well-being?**
   - At what level of beer consumption (light, moderate, heavy) do negative effects on happiness, sleep, and social engagement become apparent?

3. **Does attending more social events influence beer consumption and well-being?**
   - Do students who attend more social gatherings drink more beer? How does this relate to their happiness and academic performance?

4. **What advice can be given to students based on the findings?**
   - Based on the analysis, what advice should be given to students to maintain a healthy balance between social life, academic success, and well-being?

## Optional Frontend:
Build a **"Student Well-Being Dashboard"** that allows users to:
- Visualise the relationship between beer consumption and GPA.
- Track their own happiness, sleep, and social life based on their drinking habits.
- Identify trends in beer consumption and how it correlates with academic and social life.

## Expected Outcome:
At the end of this case study, you should be able to:
- Identify the relationship between beer consumption and academic performance.
- Assess the effects of beer consumption on happiness, sleep quality, and social engagement.
- Provide insights into whether attending more social events leads to higher beer consumption and if this impacts well-being.
- Make recommendations to students about how they can balance social drinking with their academic responsibilities and well-being.


