# gradereports/GradeReport.py

from students.StudentService import find_student
from courses.CourseService import find_course
from results.ResultService import results

grade_points = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D": 1.0,
    "F": 0.0
}

def calculate_gpa(student_id):
    student_results = [r for r in results if r["student_id"] == student_id]

    if not student_results:
        print("No results found for this student.")
        return None

    total_credits = 0
    total_points = 0

    for r in student_results:
        course = find_course(r["course_code"])
        if not course:
            continue

        credit = course["credit"]
        grade = r["grade"]

        total_credits += credit
        total_points += credit * grade_points[grade]

    if total_credits == 0:
        return 0

    return round(total_points / total_credits, 2)


def generate_report(student_id):
    student = find_student(student_id)

    if not student:
        print("Student not found!")
        return

    print(f"\n--- Grade Report for {student['full_name']} (ID: {student['id']}) ---")
    print("Course\tTitle\tCredit\tGrade")
    print("-" * 40)

    student_results = [r for r in results if r["student_id"] == student_id]

    for r in student_results:
        course = find_course(r["course_code"])
        if course:
            print(f"{course['code']}\t{course['title']}\t{course['credit']}\t{r['grade']}")

    gpa = calculate_gpa(student_id)
    print(f"\nCumulative GPA: {gpa}")