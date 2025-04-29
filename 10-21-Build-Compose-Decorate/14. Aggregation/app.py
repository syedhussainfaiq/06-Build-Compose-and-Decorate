class Employee:
    def __init__(self, emp_id, name, position):
        self.emp_id = emp_id
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")

class Department:
    def __init__(self, dept_id, dept_name):
        self.dept_id = dept_id
        self.dept_name = dept_name
        self.employees = []  # A list to hold references to Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_department_info(self):
        print(f"Department ID: {self.dept_id}")
        print(f"Department Name: {self.dept_name}")
        print("Employees:")
        for emp in self.employees:
            print(f"  - {emp.name} ({emp.position})")

# Example usage
# Create independent Employee objects
emp1 = Employee(101, "Hussain", "Developer")
emp2 = Employee(102, "Fariz", "Designer")

# Create a Department object and aggregate employees
dept = Department(1, "IT Department")
dept.add_employee(emp1)
dept.add_employee(emp2)

# Display information
print("Employee Details:")
emp1.display_info()
emp2.display_info()
print("\nDepartment Details:")
dept.display_department_info()
