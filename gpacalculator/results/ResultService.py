# results/ResultService.py

results = []

from students.StudentService import find_student
from courses.CourseService import find_course

def add_result():
    try:
        student_id = input("Enter Student ID: ").strip()
        student = find_student(student_id)

        if not student:
            print("Student not found!")
            return

        course_code = input("Enter Course Code: ").strip()
        course = find_course(course_code)

        if not course:
            print("Course not found!")
            return

        grade = input("Enter Grade (A+, A, A-, B+, B, B-, C+, C, C-, D, F): ").strip().upper()

        if grade not in ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]:
            print("Invalid grade!")
            return

        for r in results:
            if r["student_id"] == student_id and r["course_code"] == course_code:
                r["grade"] = grade
                print("Result updated successfully!")
                return

        results.append({
            "student_id": student_id,
            "course_code": course_code,
            "grade": grade
        })

        print("Result added successfully!")

    except Exception as e:
        print(f"Error adding result: {e}")


def list_results(student_id=None):
    filtered = results

    if student_id:
        filtered = [r for r in results if r["student_id"] == student_id]

    if not filtered:
        print("No results found.")
        return

    print("\nResults:")
    print("Student ID\tCourse Code\tGrade")
    print("-" * 40)

    for r in filtered:
        print(f"{r['student_id']}\t{r['course_code']}\t{r['grade']}")