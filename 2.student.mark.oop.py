class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.marks = {}

    def input_marks(self):
        num_subjects = int(input("Enter number of subjects: "))
        for i in range(num_subjects):
            subject_name = input("Enter subject name: ")
            mark = float(input("Enter mark for {}: ".format(subject_name)))
            self.marks[subject_name] = mark

    def display_record(self):
        print(self.name, "-", self.student_id)
        for subject, mark in self.marks.items():
            print(subject, "-", mark)
        print()

class StudentRecord:
    def __init__(self):
        self.records = {}

    def add_student(self):
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        student = Student(student_name, student_id)
        student.input_marks()
        self.records[(student_name, student_id)] = student

    def remove_student(self):
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        if (student_name, student_id) in self.records:
            del self.records[(student_name, student_id)]
        else:
            print("Student not found")

    def display_records(self):
        for student in self.records.values():
            student.display_record()

if __name__ == '__main__':
    student_record = StudentRecord()

    while True:
        print("Enter 1 to add a student")
        print("Enter 2 to remove a student")
        print("Enter 3 to display all records")
        print("Enter 4 to exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_record.add_student()
        elif choice == 2:
            student_record.remove_student()
        elif choice == 3:
            student_record.display_records()
        elif choice == 4:
            break
        else:
            print("Invalid choice")