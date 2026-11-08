# Student Feedback Analyzer

## Project Details

- **Student Name:** PRIYA SINGH
- **ERP Number:** RU-26-00006
- **Course:** BCA 1 B
- **Project Statement:** PS No. 93
- **Programming Language:** Python 3

## Project Description

The Student Feedback Analyzer reads student feedback from `feedback.csv` using Pandas. It validates ratings, calculates the average rating and rating distribution, identifies the top three words in comments, and analyzes feedback sentiment.

## Features

1. Reads feedback records from a CSV file.
2. Validates ratings as whole numbers from 1 to 5 and skips invalid rows with a warning.
3. Calculates the average rating.
4. Displays the count for each rating from 1 to 5.
5. Finds the top three words in feedback comments after removing stop words.
6. Groups feedback into Positive (ratings 4–5), Neutral (rating 3), and Negative (ratings 1–2).
7. Displays a bar chart of sentiment counts.
8. Handles a missing `feedback.csv` file with an error message.

## Requirements

- Python 3
- Pandas
- Matplotlib

## Install Required Libraries

Open a terminal in the project folder and run:

```bash
python -m pip install pandas matplotlib
```

## Project Files

Keep these files in the same folder:

- `one.py` — main Python program
- `feedback.csv` — feedback input data
- `README.md` — project documentation
- `Test_cases_passed.pdf` — test case report
- `PS_No_93_Project_Details.png` — project allocation screenshot

## CSV Format

The CSV file must contain these three columns:

```csv
StudentID,Rating,Comment
S1,5,Great teaching and clear notes
S2,4,Clear explanations and good examples
```

Ratings must be whole numbers from 1 to 5. Invalid rows are skipped with a warning.

## How to Run

1. Open the project folder in VS Code.
2. Make sure `one.py` and `feedback.csv` are in the same folder.
3. Install the required libraries.
4. Run:

```bash
python one.py
```

## Menu Options

1. **Summary and Top 3 Words** — displays valid feedback count, average rating, rating distribution, and the three most frequent comment words.
2. **Sentiment Analysis** — displays Positive, Neutral, and Negative percentages and a bar chart.
3. **Exit** — closes the program.
