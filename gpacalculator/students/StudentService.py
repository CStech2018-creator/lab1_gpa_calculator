"""
StudentService.py
Provides functions to manage students.
Demonstrates module-level global container and functions that accept
an external container for testability.
"""

from typing import List, Dict, Optional

# Module-level global list of students (demonstrates use of global variables)
# Each student: {"id": str, "name": str}
STUDENTS: List[Dict[str, str]] = []

def _next_student_id() -> str:
    """Generate next student id as a string (1-based)."""
    return str(len(STUDENTS) + 1)

def add_student(name: str, container: Optional[List[Dict[str, str]]] = None) -> str:
    """
    Add a new student.
    If container is provided, use that list; otherwise use module-level STUDENTS.
    Returns the student id.
    """
    if container is None:
        container = STUDENTS

    sid = str(len(container) + 1)
    container.append({"id": sid, "name": name.strip()})
    return sid

def list_students(container: Optional[List[Dict[str, str]]] = None):
    """Print the list of registered students."""
    if container is None:
        container = STUDENTS
    if not container:
        print("No students registered yet.")
        return
    print("Registered students:")
    for s in container:
        print(f"  ID: {s['id']}\tName: {s['name']}")

def find_student_by_id(student_id: str, container: Optional[List[Dict[str, str]]] = None) -> Optional[Dict[str, str]]:
    """Return student dict if found, else None."""
    if container is None:
        container = STUDENTS
    for s in container:
        if s["id"] == student_id:
            return s
    return None
