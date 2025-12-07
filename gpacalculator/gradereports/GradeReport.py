"""
GradeReport.py
Converts DBU letter grades to grade points and produces GPA reports.
"""

from typing import Dict, List, Optional
from students.StudentService import STUDENTS, find_student_by_id
from courses.CourseService import COURSES, find_course_by_code
from results.ResultService import RESULTS, list_results_for_student

# DBU grade conversion table
GRADE_SCALE = {
    "A": 4.00,
    "A-": 3.75,
    "B+": 3.50,
    "B": 3.00,
    "B-": 2.75,
    "C+": 2.50,
    "C": 2.00,
    "C-": 1.75,
    "D": 1.00,
    "F": 0.00
}

def grade_point(letter: str) -> float:
    """
    Convert letter grade to DBU grade point.
    Unknown letters map to 0.0.
    """
    if letter is None:
        return 0.0
    key = letter.strip().upper()
    return GRADE_SCALE.get(key, 0.0)

def calculate_gpa(student_id: str) -> Dict:
    """
    Calculate GPA for a student and return a report dict:
    {
        "student": {"id":..., "name":...},
        "courses": [{"code":..., "title":..., "credit":..., "letter":..., "gp":...}, ...],
        "total_credits": float,
        "total_grade_points": float,
        "gpa": float
    }
    """
    student = find_student_by_id(student_id)
    if not student:
        raise ValueError("Student not found")

    student_results = list_results_for_student(student_id)
    courses_info = []
    total_credits = 0.0
    total_grade_points = 0.0

    # Build a set of course codes to avoid duplicates when student has repeated entries
    seen_courses = set()

    for r in student_results:
        code = r["cid"].strip().upper()
        # skip duplicate entries for the same course (use latest entry instead)
        if code in seen_courses:
            # We'll allow duplicates but treat them as separate registrations if needed.
            pass
        seen_courses.add(code)

        course = find_course_by_code(code)
        if not course:
            # Unknown course definition: skip entry
            continue

        credit = float(course["credit"])
        gp = float(r.get("gp", grade_point(r.get("letter", ""))))
        total_credits += credit
        total_grade_points += gp * credit

        courses_info.append({
            "code": code,
            "title": course["title"],
            "credit": credit,
            "letter": r.get("letter", ""),
            "gp": gp
        })

    gpa = 0.0
    if total_credits > 0:
        gpa = total_grade_points / total_credits

    return {
        "student": student,
        "courses": courses_info,
        "total_credits": total_credits,
        "total_grade_points": total_grade_points,
        "gpa": gpa
    }

def format_grade_report(report: Dict) -> str:
    """Return a nice-formatted string of the grade report."""
    student = report["student"]
    lines = []
    lines.append(f"Grade Report for {student['name']} (ID: {student['id']})")
    lines.append("-" * 50)
    if not report["courses"]:
        lines.append("No course results recorded.")
    else:
        lines.append(f"{'Code':8}{'Title':30}{'Cr':>4}{'Letter':>8}{'GP':>6}")
        for c in report["courses"]:
            title = (c["title"][:27] + "...") if len(c["title"]) > 30 else c["title"]
            lines.append(f"{c['code']:8}{title:30}{c['credit']:4.1f}{c['letter']:>8}{c['gp']:6.2f}")
        lines.append("-" * 50)
        lines.append(f"Total Credits: {report['total_credits']:.2f}")
        lines.append(f"Total Grade Points: {report['total_grade_points']:.2f}")
        lines.append(f"CGPA: {report['gpa']:.3f}")
    return "\n".join(lines)
