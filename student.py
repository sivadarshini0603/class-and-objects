class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = ""
        self.marks = []
        self.total = 0
        self.average = 0
        self.grade = ""

    def get_details(self):
        self.name = input("Enter name: ")
        self.roll_no = input("Enter roll number: ")
        for i in range(5):
            print("Enter mark", i + 1, ": ", end="")
            mark = float(input())
            self.marks.append(mark)

    def calculate(self):
        self.total = sum(self.marks)
        self.average = self.total / 5
        if self.average >= 90:
            self.grade = "A+"
        elif self.average >= 80:
            self.grade = "A"
        elif self.average >= 70:
            self.grade = "B"
        elif self.average >= 60:
            self.grade = "C"
        elif self.average >= 50:
            self.grade = "D"
        else:
            self.grade = "F"

    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("Total:", self.total)
        print("Average:", self.average)
        print("Grade:", self.grade)
s = Student()
s.get_details()
s.calculate()
s.display()
