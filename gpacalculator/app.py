# app.py

from students.StudentService import register_student, list_students
from courses.CourseService import add_course, list_courses
from results.ResultService import add_result, list_results
from gradereports.GradeReport import generate_report

def main_menu():
    while True:
        print("\n=== GPA CALCULATOR ===")
        print("1. Students")
        print("2. Courses")
        print("3. Results")
        print("4. Grade Reports")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            student_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            result_menu()
        elif choice == "4":
            report_menu()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid option!")


def student_menu():
    while True:
        print("\n--- Students Menu ---")
        print("1. Register Student")
        print("2. List Students")
        print("3. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            break
        else:
            print("Invalid option!")


def course_menu():
    while True:
        print("\n--- Courses Menu ---")
        print("1. Add Course")
        print("2. List Courses")
        print("3. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_course()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            break
        else:
            print("Invalid option!")


def result_menu():
    while True:
        print("\n--- Results Menu ---")
        print("1. Add Result")
        print("2. List Student Results")
        print("3. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_result()
        elif choice == "2":
            student_id = input("Enter Student ID: ").strip()
            list_results(student_id)
        elif choice == "3":
            break
        else:
            print("Invalid option!")


def report_menu():
    student_id = input("Enter Student ID: ").strip()
    generate_report(student_id)


if __name__ == "main":
    main_menu()