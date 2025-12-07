"""
ResultService.py
Manages results (student-course-grade entries).
Validates student and course existence before adding results.
"""

from typing import List, Dict, Optional
from students.StudentService import STUDENTS, find_student_by_id
from courses.CourseService import COURSES, find_course_by_code

# Module-level results container
# Each result: {"sid": str, "cid": str, "letter": str, "gp": float}
RESULTS: List[Dict[str, object]] = []

def add_result(student_id: str, course_code: str, letter_grade: str, grade_point: float, container: Optional[List[Dict]] = None) -> bool:
    """
    Add a result entry after validating student and course.
    Returns True if added, False otherwise.
    """
    if container is None:
        container = RESULTS

    # Validate student & course
    if not find_student_by_id(student_id, STUDENTS):
        return False
    if not find_course_by_code(course_code, COURSES):
        return False

    # Normalize
    entry = {
        "sid": student_id,
        "cid": course_code.strip().upper(),
        "letter": letter_grade.strip().upper(),
        "gp": float(grade_point)
    }
    container.append(entry)
    return True

def list_results_for_student(student_id: str, container: Optional[List[Dict]] = None) -> List[Dict]:
    """Return list of results for a given student id."""
    if container is None:
        container = RESULTS
    return [r for r in container if r["sid"] == student_id]

def list_all_results(container: Optional[List[Dict]] = None):
    """Print all results in a readable fashion."""
    if container is None:
        container = RESULTS
    if not container:
        print("No results recorded yet.")
        return
    for r in container:
        print(f"Student {r['sid']}\tCourse {r['cid']}\tGrade {r['letter']}\tGP: {r['gp']}")
