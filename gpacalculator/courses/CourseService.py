# courses/CourseService.py

courses = []

def add_course():
    try:
        course_code = input("Enter Course Code: ").strip()
        for c in courses:
            if c["code"] == course_code:
                print("Course code already exists!")
                return

        title = input("Enter Course Title: ").strip()
        credit = float(input("Enter Course Credit: ").strip())

        courses.append({
            "code": course_code,
            "title": title,
            "credit": credit
        })

        print(f"Course {title} added successfully!")

    except Exception as e:
        print(f"Error adding course: {e}")


def list_courses():
    if not courses:
        print("No courses added yet.")
        return

    print("\nAvailable Courses:")
    print("Code\tTitle\tCredit")
    print("-" * 40)

    for c in courses:
        print(f"{c['code']}\t{c['title']}\t{c['credit']}")


def find_course(course_code):
    for c in courses:
        if c["code"] == course_code:
            return c
    return None