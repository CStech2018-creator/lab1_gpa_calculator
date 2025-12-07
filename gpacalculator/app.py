# Import your services
from students.StudentService import add_student, list_students, find_student_by_id, STUDENTS
from courses.CourseService import add_course, list_courses
from results.ResultService import add_result, list_results_for_student, list_all_results, RESULTS
from gradereports.GradeReport import calculate_gpa, format_grade_report

# Simple pause function
def pause():
    input("\nPress Enter to continue...")

# DBU grading system thresholds
def get_letter_grade(marks: float) -> str:
    if marks >= 90:
        return "A⁺"
    elif marks >= 85:
        return "A"
    elif marks >= 80:
        return "A⁻"
    elif marks >= 75:
        return "B⁺"
    elif marks >= 70:
        return "B"
    elif marks >= 65:
        return "B⁻"
    elif marks >= 60:
        return "C⁺"
    elif marks >= 50:
        return "C"
    else:
        return "F"

GRADE_SCALE = {
    "A⁺": 4.0,
    "A": 4.0,
    "A⁻": 3.75,
    "B⁺": 3.5,
    "B": 3.0,
    "B⁻": 2.75,
    "C⁺": 2.5,
    "C": 2.0,
    "F": 0.0
}

# Main menu function
def main_menu():
    while True:
        print("\n==== GPA CALCULATOR ====")
        print("1. Students")
        print("2. Courses")
        print("3. Results")
        print("4. Grade Report")
        print("5. Show all data (debug)")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        # ------------------- Students -------------------
        if choice == "1":
            while True:
                print("\n--- Students Menu ---")
                list_students()

                print("\nOptions:")
                print("1. Add new student")
                print("2. Find student by ID")
                print("3. Back to main menu")

                student_choice = input("Enter choice: ").strip()

                if student_choice == "1":
                    name = input("\nEnter new student name (or leave blank to skip): ").strip()
                    if name:
                        if any(char.isdigit() for char in name):
                            print("Invalid name! Names cannot contain numbers.")
                        else:
                            sid = add_student(name)
                            print(f"Added student: {name} (ID: {sid})")
                            print("Current STUDENTS list:", STUDENTS)
                    pause()

                elif student_choice == "2":
                    search_input = input("\nEnter student ID to search: ").strip()
                    if search_input:
                        student = find_student_by_id(search_input)
                        if student:
                            print(f"Found student → ID: {student['id']}, Name: {student['name']}")
                        else:
                            print("Student not found!")
                    pause()

                elif student_choice == "3":
                    break

                else:
                    print("Invalid choice. Please try again.")

        # ------------------- Courses -------------------
        elif choice == "2":
            print("\n--- Courses ---")
            list_courses()
            code = input("\nEnter course code (or leave blank to skip): ").strip()
            if code:
                title = input("Enter course title: ").strip()
                while True:
                    try:
                        credit = float(input("Enter credit hours: ").strip())
                        if credit <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid credit. Enter a positive number.")
                add_course(code, title, credit)
                print(f"Added course: {code} - {title} ({credit}cr)")
            pause()

        # ------------------- Results -------------------
        elif choice == "3":
            from courses.CourseService import find_course_by_code

            while True:
                print("\n--- Results Menu ---")
                print("1. Register student result")
                print("2. List all results")
                print("3. Back to main menu")

                result_choice = input("Enter choice: ").strip()

                if result_choice == "1":
                    # Select student
                    list_students()
                    student_id = input("Enter student ID: ").strip()
                    student = find_student_by_id(student_id)
                    if not student:
                        print("Student not found!")
                        pause()
                        continue

                    # Select course
                    list_courses()
                    course_code = input("Enter course code: ").strip().upper()
                    course = find_course_by_code(course_code)
                    if not course:
                        print("Course not found!")
                        pause()
                        continue

                    # Check for duplicate result
                    duplicate = any(r["sid"] == student_id and r["cid"] == course_code for r in RESULTS)
                    if duplicate:
                        print(f"Result already exists for Student {student['name']} in Course {course_code}.")
                        pause()
                        continue

                    # Enter marks
                    try:
                        marks = float(input("Enter marks (0-100): ").strip())
                        if not (0 <= marks <= 100):
                            raise ValueError
                    except ValueError:
                        print("Invalid marks.")
                        pause()
                        continue

                    # Convert marks to letter grade and GP
                    letter = get_letter_grade(marks)
                    gp = GRADE_SCALE[letter]

                    success = add_result(student_id, course_code, letter, gp)
                    if success:
                        print(f"Result recorded: Student {student['name']}, Course {course_code}, Grade {letter}, GP {gp}")
                    else:
                        print("Failed to add result. Check student ID and course code.")
                    pause()

                elif result_choice == "2":
                    list_all_results()
                    pause()

                elif result_choice == "3":
                    break

                else:
                    print("Invalid choice.")

        # ------------------- Grade Report -------------------
        elif choice == "4":
            print("\n--- Grade Report ---")
            list_students()
            student_id = input("\nEnter student ID to generate grade report: ").strip()
            student = find_student_by_id(student_id)
            if not student:
                print("Student not found!")
            else:
                try:
                    report = calculate_gpa(student_id)
                    formatted = format_grade_report(report)
                    print("\n" + formatted)
                except Exception as e:
                    print("Error generating grade report:", str(e))
            pause()

        # ------------------- Show all data (debug) -------------------
        elif choice == "5":
            print("\n--- All Data (Debug) ---")
            print("\nStudents:")
            list_students()
            print("\nCourses:")
            list_courses()
            print("\nResults:")
            list_all_results()
            pause()

        # ------------------- Exit -------------------
        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main_menu()
