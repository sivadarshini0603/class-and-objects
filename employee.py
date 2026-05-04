class Employee:
    def __init__(self):
        self.emp_id = ""
        self.name = ""
        self.basic = ""
        self.da = 0
        self.hra = 0
        self.gross_salary = 0
    def get_details(self):
        self.emp_id = int(input("ENTER EMPLOYEE ID:"))
        self.name = input("ENTER NAME:")
        self.basic = int(input("ENTER BASIC SALARY:"))
    def calculate(self):
        self.da = 0.10 * self.basic  # 10% of basic pay
        self.hra = 0.20 * self.basic  # 20% of basic pay
        self.gross_salary = self.basic + self.da + self.hra

    def display(self):
        print("---------EMPLOYEE DETAILS---------")
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic:", self.basic)
        print("DA:", self.da)
        print("HRA:", self.hra)
        print("GROSS SALARY:",self.gross_salary)
s=Employee()
s.get_details()
s.calculate()
s.display()
