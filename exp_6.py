faculty_dict = {
    'faculty_id1': {'name': 'ABC', 'department': 'Computer Science'},
    'faculty_id2': {'name': 'EFG', 'department': 'Mathematics'}
}

students_dict = {
    'student_id1': {'name': 'PQR', 'major': 'Physics'},
    'student_id2': {'name': 'XYZ', 'major': 'History'}
}

faculty_list = list(faculty_dict.values())
students_list = list(students_dict.values())

print("Faculty List: ")
for faculty in faculty_list:
    print(f"name: {faculty['name']}, Department: {faculty['department']}")

print("\nStudents List: ")
for student_id, student in students_dict.items():
    print(f"name: {student['name']}, Major: {student['major']}")
