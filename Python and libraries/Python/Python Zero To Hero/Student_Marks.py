from functools import reduce

class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = list(marks)

        self.total = 0
        self.percen = 0
        self.grade = ""
        self.remark = ''

    def calculate_marks(self):
        self.total = reduce(lambda x, y: x + y, self.marks)
        return self.total
    
    def percentage(self):
        self.percen = self.total / (len(self.marks)*100) * 100
        return self.percen

    def calculate_grade(self):

        if self.percen >= 90:
            self.grade = "Grade A"
            self.remark = "PASS"

        elif self.percen >= 75:
            self.grade = "Grade B"
            self.remark = "PASS"

        elif self.percen >= 60:
            self.grade = "Grade C"
            self.remark = "PASS"

        elif self.percen >= 40:
            self.grade = "Grade D"
            self.remark = "FAIL"

        else:
            self.grade = "Fail"
            self.remark = "FAIL"

        return (self.grade, self.remark)
    
    def show_result(self):

        print("====== Student Result ======\n")    

        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll_no}")
        print(f"Total Marks : {self.total}/{(len(self.marks)*100)}")
        print(f"Percentage : {self.percen}%")
        print(f"Grade : {self.grade}")
        print(f"Result : {self.remark}\n")

student = Student('Danish', 100, [98, 97, 89, 99, 90])
student1 = Student("Mubashishir", 101, [80, 75, 90])
student2 = Student("Sohel", 102, [60, 65, 70])
student3 = Student("Aman", 103, [30, 35, 40])

students = [student, student1, student2, student3]

for i in students:
    i.calculate_marks()
    i.percentage()
    i.calculate_grade()
    i.show_result()


topper = max(students, key= lambda x : x.total)

print('====== Class Topper ======\n')
print(f"Name: {topper.name}")
print(f"Percestage : {topper.percen}")

topper = min(students, key=lambda s: s.total)

print("\n===== Fail Student =====\n")
print(f"Name: {topper.name}")
print(f"Total Marks: {topper.percen}")  

print()

Search_roll = int(input("Enter Your Roll No."))

found = False

for i in students:

    if i.roll_no == Search_roll:
        i.show_result()
        found = True
        break

if not found:
    print("Student Not Found")