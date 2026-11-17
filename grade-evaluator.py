import csv
import sys
import os

def load_csv_data():
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    print("\n--- Processing Grades ---")

    if len(data) == 0:
        print("Error: the file has no assignments.")
        return

    # a) scores must be between 0 and 100
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(f"Error: score for '{item['assignment']}' is {item['score']}, it must be between 0 and 100.")
            return

    # b) weights must add up correctly
    total_weight = 0
    formative_weight = 0
    summative_weight = 0
    for item in data:
        total_weight += item['weight']
        if item['group'] == 'Formative':
            formative_weight += item['weight']
        elif item['group'] == 'Summative':
            summative_weight += item['weight']

    if total_weight != 100:
        print(f"Error: total weight is {total_weight}, it must be 100.")
        return
    if formative_weight != 60:
        print(f"Error: Formative weight is {formative_weight}, it must be 60.")
        return
    if summative_weight != 40:
        print(f"Error: Summative weight is {summative_weight}, it must be 40.")
        return

    # c) final grade and GPA
    formative_points = 0
    summative_points = 0
    for item in data:
        points = item['score'] * item['weight'] / 100
        if item['group'] == 'Formative':
            formative_points += points
        else:
            summative_points += points

    total_grade = formative_points + summative_points
    gpa = (total_grade / 100) * 5.0

    formative_percent = formative_points / formative_weight * 100
    summative_percent = summative_points / summative_weight * 100

    print(f"Formative: {formative_percent:.1f}%")
    print(f"Summative: {summative_percent:.1f}%")
    print(f"Final Grade: {total_grade:.1f}/100")
    print(f"GPA: {gpa:.2f}")

    # d) pass only if both categories are 50% or more
    if formative_percent >= 50 and summative_percent >= 50:
        status = "PASSED"
    else:
        status = "FAILED"

    # e) failed formative assignments with the highest weight
    failed = []
    for item in data:
        if item['group'] == 'Formative' and item['score'] < 50:
            failed.append(item)

    resubmit = []
    if len(failed) > 0:
        highest = failed[0]['weight']
        for item in failed:
            if item['weight'] > highest:
                highest = item['weight']
        for item in failed:
            if item['weight'] == highest:
                resubmit.append(item)

    # f) final decision
    print(f"\nFinal Status: {status}")
    if len(resubmit) > 0:
        print("Eligible for resubmission:")
        for item in resubmit:
            print(f"- {item['assignment']}")
    else:
        print("No assignments to resubmit.")

if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
