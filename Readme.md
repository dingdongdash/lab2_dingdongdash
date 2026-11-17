# Lab 2: ALU Transcript Generator

Files: `grade-evaluator.py`, `organizer.sh`, `grades.csv`

## grade-evaluator.py
Reads a grades CSV file and prints the final grade, GPA, PASSED/FAILED status and which assignments can be resubmitted.

The CSV needs these columns: `assignment,group,score,weight`
- `group` is Formative or Summative
- `score` is between 0 and 100

Checks it does:
- every score is between 0 and 100
- weights are not negative
- all weights add up to 100 (Formative 60, Summative 40)
- GPA = (Total Grade / 100) * 5.0
- PASSED only if both Formative and Summative are 50% or more
- failed Formative assignments (below 50) with the highest weight can be resubmitted (all of them if there is a tie)

Run it from the folder with the CSV:

    python3 grade-evaluator.py

Then type `grades.csv` when asked for the file name.

Example output:

    Formative: 56.7%
    Summative: 65.0%
    Final Grade: 60.0/100
    GPA: 3.00

    Final Status: PASSED
    Eligible for resubmission:
    - Group Exercise
    - Functions and Debugging Lab

If something is wrong with the file (missing, empty, bad numbers, wrong weights) it prints an error message.

## organizer.sh
Moves `grades.csv` into the `archive` folder with a timestamp in the name (e.g. `grades_20251105-170000.csv`), creates a new empty `grades.csv`, and adds a line to `organizer.log`.

Run it:

    ./organizer.sh
