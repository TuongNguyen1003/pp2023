# 1.student.mark.py

# Function to input student details
def input_student():
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    return (student_name, student_id)

# Function to input marks for a student
def input_marks():
    marks = {}
    num_subjects = int(input("Enter number of subjects: "))
    for i in range(num_subjects):
        subject_name = input("Enter subject name: ")
        mark = float(input("Enter mark for {}: ".format(subject_name)))
        marks[subject_name] = mark
    return marks

# Function to add a student to the record
def add_student(records):
    student = input_student()
    marks = input_marks()
    records[student] = marks

# Function to remove a student from the record
def remove_student(records):
    student = input_student()
    if student in records:
        del records[student]
    else:
        print("Student not found")

# Function to display all the records
def display_records(records):
    for student, marks in records.items():
        print(student[0], "-", student[1])
        for subject, mark in marks.items():
            print(subject, "-", mark)
        print()

# Main program
records = {}
while True:
    print("Enter 1 to add a student")
    print("Enter 2 to remove a student")
    print("Enter 3 to display all records")
    print("Enter 4 to exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student(records)
    elif choice == 2:
        remove_student(records)
    elif choice == 3:
        display_records(records)
    elif choice == 4:
        break
    else:
        print("Invalid choice")
