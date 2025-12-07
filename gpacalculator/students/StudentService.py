#THUS  ALL. ARE THE. STUDENT GPA 
    # students/StudentService.py

students = []  # Global list to store students

def register_student():
    try:
        student_id = input("Enter Student ID: ").strip()
        for s in students:
            if s["id"] == student_id:
                print("Student ID already exists!")
                return

        first_name = input("Enter First Name: ").strip()
        last_name = input("Enter Last Name: ").strip()
        department = input("Enter Department (e.g., CS, IT, SE): ").strip()
        year = input("Enter Year (1, 2, 3, 4): ").strip()

        full_name = f"{first_name} {last_name}"

        students.append({
            "id": student_id,
            "first_name": first_name,
            "last_name": last_name,
            "full_name": full_name,
            "department": department,
            "year": year
        })

        print(f"Student {full_name} registered successfully!")

    except Exception as e:
        print(f"Error registering student: {e}")


def list_students():
    if not students:
        print("No students registered yet.")
        return

    print("\nRegistered Students:")
    print("ID\tFull Name\tDepartment\tYear")
    print("-" * 50)

    for s in students:
        print(f"{s['id']}\t{s['full_name']}\t{s['department']}\t{s['year']}")


def find_student(student_id):
    for s in students:
        if s["id"] == student_id:
            return s
    return None