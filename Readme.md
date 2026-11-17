# Lab 2: ALU Transcript Generator

## grade-evaluator.py
Reads a grades CSV file, checks the scores and weights, then prints the final grade, GPA, PASSED/FAILED status and which assignments can be resubmitted.

Run it:

    python3 grade-evaluator.py

Then type `grades.csv` when asked for the file name.

## organizer.sh
Moves `grades.csv` into the `archive` folder with a timestamp in the name, creates a new empty `grades.csv`, and writes a line to `organizer.log`.

Run it:

    ./organizer.sh
