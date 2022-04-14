# 20CS031 - DITSA MANDANI
# Repo. Link - https://github.com/Ditsa1/CE259-PIP-20SC031

# creating student class
class student:
    Name = 'Ditsa'
    rollNumber = 0

    # function to set the id and name
    def details(self, rollNumber, Name):
        self.Name = Name
        self.rollNumber = rollNumber


# creating class from another class
class exam(student):
    marks_list = []

    # to set the marks of student
    def marks(self, marks_list):
        self.marks_list = marks_list
        return marks_list


# creating class result from exam
class result(exam):
    marks_gain = 0

    # gives total marks of student
    def result_of_student(self, marks_gain):
        total_marks = 0
        for item in marks_gain:
            total_marks += item
        return total_marks


# object of result class
sobj = result()
student_name = input("Enter the name of the student: ")
student_id = input("Enter the Roll Number of the student: ")

sobj.details(student_id, student_name)
print(f"Enter the marks of {student_name} in 6 subject: \n")
marks = []
for i in range(0, 6):
    marks.append(int(input()))

marks_obtain = sobj.marks(marks)
total = sobj.result_of_student(marks_obtain)
print(f"Total of {student_name}'s marks is: {total}")
