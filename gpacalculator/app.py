import os
import sys
from students.StudentService import register_student, list_students
from courses.CourseService import register_course, list_courses
from results.ResultService import register_result, get_results_by_student
from gradereports.GradeReport import calculate_gpa


def main_menu():
    while True:
        print("\n==== GPA CALCULATOR ====")
        print("1. Students")
        print("2. Courses")
        print("3. Results")
        print("4. Grade Reports")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n--- STUDENTS ---")
            list_students()
            register_student()

        elif choice == "2":
            print("\n--- COURSES ---")
            list_courses()
            register_course()

        elif choice == "3":
            print("\n--- RESULTS ---")
            sid = input("Enter student ID: ")
            register_result(sid)

        elif choice == "4":
            print("\n--- GRADE REPORT ---")
            calculate_gpa()

        elif choice == "5":
            print("Bye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "main":
    main_menu()