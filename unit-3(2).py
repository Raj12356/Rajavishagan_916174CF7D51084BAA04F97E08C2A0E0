print("^^^^!!!!SORT_METHOD!!!!^^^^")
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

students = [
    Student("Raja", "001", 3.9),
    Student("dhanush", "002", 3.7),
    Student("vinith", "003", 3.8),
    Student("sakthi", "004", 3.6),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")