"""
courses package - CourseService for managing courses.
"""

class CourseService:
    def init(self):
        # Stores courses as a list of dictionaries
        # Example: {"code": "CSC101", "title": "Intro", "credit": 3}
        self.courses = []

    def add_course(self, code: str, title: str, credit: float) -> bool:
        """Add a course if the code does not exist."""
        code = code.strip().upper()

        if self.find_course_by_code(code):
            return False  # duplicate

        self.courses.append({
            "code": code,
            "title": title.strip(),
            "credit": float(credit)
        })
        return True

    def list_courses(self):
        """Print registered courses."""
        if not self.courses:
            print("No courses registered yet.")
            return

        print("Registered Courses:")
        for course in self.courses:
            print(f"{course['code']}  {course['title']}  Credits: {course['credit']}")

    def find_course_by_code(self, code: str):
        """Return course dict if found."""
        code = code.strip().upper()
        for c in self.courses:
            if c["code"] == code:
                return c
        return None