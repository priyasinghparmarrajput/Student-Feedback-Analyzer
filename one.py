# Student Name          : Priya Singh
# ERP Number            : RU-26-00006
# Course                : BCA 1 B
# Programming Language  : Python 3
# Project                : Student Feedback Analyzer (PS No. 93)

import os
import re
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "feedback.csv")

STOP_WORDS = {
    "and", "but", "the", "is", "a", "of", "to", "was", "were", "in",
    "for", "with", "it", "this", "that", "very", "are", "an", "on"
}


def load_feedback():
    """Read and validate feedback records from the CSV file."""
    if not os.path.exists(FILE_NAME):
        print("Error: feedback.csv file not found.")
        return None

    try:
        df = pd.read_csv(FILE_NAME)
    except Exception as error:
        print(f"Error reading feedback.csv: {error}")
        return None

    required_columns = {"StudentID", "Rating", "Comment"}
    if not required_columns.issubset(df.columns):
        print("Error: CSV must contain StudentID, Rating, Comment columns.")
        return None

    valid_rows = []
    for index, row in df.iterrows():
        student_id = str(row["StudentID"]).strip()
        comment = str(row["Comment"]).strip()

        try:
            rating_number = float(row["Rating"])
            is_whole_number = rating_number.is_integer()
        except (TypeError, ValueError):
            is_whole_number = False
            rating_number = 0

        if not student_id or not comment or not is_whole_number or not 1 <= rating_number <= 5:
            print(
                f"Warning: Row {index + 2} skipped - "
                "rating must be a whole number from 1 to 5."
            )
            continue

        valid_rows.append({
            "StudentID": student_id,
            "Rating": int(rating_number),
            "Comment": comment
        })

    if not valid_rows:
        print("No valid feedback records found.")
        return None

    return pd.DataFrame(valid_rows)


def get_top_words(df):
    words = []
    for comment in df["Comment"]:
        comment_words = re.findall(r"[A-Za-z]+", comment.lower())
        words.extend(word for word in comment_words if word not in STOP_WORDS)
    return Counter(words).most_common(3)


def show_summary(df):
    print("\n========== FEEDBACK SUMMARY ==========")
    print(f"Valid feedback: {len(df)}")
    print(f"Average rating: {df['Rating'].mean():.2f}")

    print("\n--- Rating Distribution ---")
    counts = df["Rating"].value_counts()
    for rating in range(5, 0, -1):
        print(f"{rating} -> {counts.get(rating, 0)}")

    print("\n--- Top 3 Words ---")
    for word, count in get_top_words(df):
        print(f"{word} ({count})")


def show_sentiment(df):
    positive = int(df["Rating"].isin([4, 5]).sum())
    neutral = int((df["Rating"] == 3).sum())
    negative = int(df["Rating"].isin([1, 2]).sum())
    total = len(df)

    print("\n========== SENTIMENT ANALYSIS ==========")
    print(f"Positive: {positive} ({positive / total * 100:.2f}%)")
    print(f"Neutral: {neutral} ({neutral / total * 100:.2f}%)")
    print(f"Negative: {negative} ({negative / total * 100:.2f}%)")

    labels = ["Positive", "Neutral", "Negative"]
    values = [positive, neutral, negative]

    plt.figure(figsize=(7, 4))
    bars = plt.bar(labels, values)
    plt.title("Student Feedback Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Feedback Records")
    plt.bar_label(bars)
    plt.tight_layout()
    plt.show()


def main():
    df = load_feedback()
    if df is None:
        return

    while True:
        print("\n========== STUDENT FEEDBACK ANALYZER ==========")
        print("1. Summary and Top 3 Words")
        print("2. Sentiment Analysis")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_summary(df)
        elif choice == "2":
            show_sentiment(df)
        elif choice == "3":
            print("Thank you for using Student Feedback Analyzer.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
