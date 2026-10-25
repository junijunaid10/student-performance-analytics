"""
Student Performance Analytics System
Domain: Python with AI
Author: Mohammad Rafiq Tantray
"""

import numpy as np
import pandas as pd


def load_dataset(filepath):
    """Loads student records from CSV into a Pandas DataFrame."""
    try:
        df = pd.read_csv(filepath)
        print(f"[SUCCESS] Loaded {len(df)} records successfully.\n")
        return df
    except FileNotFoundError:
        print(f"[ERROR] Could not find file at '{filepath}'.")
        return None


def calculate_metrics(df):
    """Calculates Total Marks and Average Marks using NumPy."""
    subjects = ["Maths", "Physics", "Chemistry"]
    marks_array = df[subjects].to_numpy()

    df["Total_Marks"] = np.sum(marks_array, axis=1)
    df["Average_Marks"] = np.round(np.mean(marks_array, axis=1), 2)
    return df


def assign_grade(avg_score):
    """Assigns letter grades based on average percentage."""
    if avg_score >= 90:
        return "A+"
    elif avg_score >= 80:
        return "A"
    elif avg_score >= 70:
        return "B"
    elif avg_score >= 60:
        return "C"
    elif avg_score >= 50:
        return "D"
    else:
        return "F"


def check_status(row):
    """Identifies pass/fail based on a minimum passing mark of 40 in each subject."""
    passing_mark = 40
    if (
        row["Maths"] >= passing_mark
        and row["Physics"] >= passing_mark
        and row["Chemistry"] >= passing_mark
    ):
        return "PASS"
    return "FAIL"


def process_student_evaluations(df):
    """Processes grading and pass/fail status using iterative loops and logic."""
    grades = []
    statuses = []

    for _, row in df.iterrows():
        grades.append(assign_grade(row["Average_Marks"]))
        statuses.append(check_status(row))

    df["Grade"] = grades
    df["Status"] = statuses
    return df


def display_analytics_summary(df):
    """Generates overall class and subject-wise performance analytics."""
    subjects = ["Maths", "Physics", "Chemistry"]

    print("=" * 65)
    print("        STUDENT PERFORMANCE ANALYTICS SUMMARY")
    print("=" * 65)

    print("\n1. Overall Class Overview:")
    print(f"   * Total Students Enrolled : {len(df)}")
    print(
        f"   * Class Overall Average   : {np.mean(df['Average_Marks'].to_numpy()):.2f}%"
    )
    print(
        f"   * Highest Average Score   : {np.max(df['Average_Marks'].to_numpy()):.2f}%"
    )
    print(
        f"   * Lowest Average Score    : {np.min(df['Average_Marks'].to_numpy()):.2f}%"
    )

    passed_count = np.sum(df["Status"].to_numpy() == "PASS")
    failed_count = len(df) - passed_count
    pass_rate = (passed_count / len(df)) * 100
    print(
        f"   * Total Passed            : {passed_count} ({pass_rate:.1f}%)"
    )
    print(f"   * Total Failed            : {failed_count}")

    print("\n2. Subject-wise Averages:")
    for subj in subjects:
        subj_avg = np.mean(df[subj].to_numpy())
        print(f"   * {subj:<12} : {subj_avg:.2f}")

    print("\n3. Top 3 Performing Students:")
    top_performers = df.sort_values(by="Total_Marks", ascending=False).head(3)
    rank = 1
    for _, student in top_performers.iterrows():
        print(
            f"   Rank {rank}: {student['Name']} ({student['Department']}) - "
            f"Total: {student['Total_Marks']}/300 | Avg: {student['Average_Marks']}% | Grade: {student['Grade']}"
        )
        rank += 1

    print("\n4. Department-wise Performance:")
    dept_summary = (
        df.groupby("Department")["Average_Marks"].mean().reset_index()
    )
    for _, dept in dept_summary.iterrows():
        print(
            f"   * Department: {dept['Department']:<6} | Mean Average: {dept['Average_Marks']:.2f}%"
        )

    print("=" * 65)


def main():
    dataset_file = "students.csv"
    data = load_dataset(dataset_file)

    if data is not None:
        data = calculate_metrics(data)
        data = process_student_evaluations(data)
        display_analytics_summary(data)


if __name__ == "__main__":
    main()
