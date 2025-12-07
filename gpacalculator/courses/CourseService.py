"""
students package - StudentService for managing students
"""

class StudentService:
    def __init__(self):
        self.students = []  # List of {"id": str, "name": str}

    def add_student(self, name: str) -> str:
        """Add a student and return the generated ID."""
        student_id = f"S{len(self.students)+1:03}"
        self.students.append({"id": student_id, "name": name.strip()})
        return student_id

    def list_students(self):
        """Print all registered students."""
        if not self.students:
            print("No students registered yet.")
            return
        print("Registered Students:")
        for s in self.students:
            print(f"{s['id']} - {s['name']}")

    def find_student_by_id(self, student_id: str):
        """Return student dict if found."""
        for s in self.students:
            if s["id"] == student_id:
                return s
        return None
