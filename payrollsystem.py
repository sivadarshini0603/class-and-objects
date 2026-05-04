class Payroll:
    def __init__(self):
        n = int(input("Enter number of employees: "))
        emp_list = []

        for i in range(n):
            emp_id = input("Enter ID: ")
            name = input("Enter Name: ")
            salary = float(input("Enter Salary: "))
            emp_list.append((emp_id, name, salary))

        self.employees = tuple(emp_list)

    def display(self):
        print("\nEmployee Details:")
        for e in self.employees:
            print(e)

    def search(self):
        key = input("\nEnter ID to search: ")
        for e in self.employees:
            if e[0] == key:
                print("Found:", e)
                return
        print("Not Found")

    def highest(self):
        max_emp = self.employees[0]
        for e in self.employees:
            if e[2] > max_emp[2]:
                max_emp = e
        print("\nHighest Salary:", max_emp)

    def above50000(self):
        print("\nSalary > 50000:")
        for e in self.employees:
            if e[2] > 50000:
                print(e)
p = Payroll()
p.display()
p.search()
p.highest()
p.above50000()
