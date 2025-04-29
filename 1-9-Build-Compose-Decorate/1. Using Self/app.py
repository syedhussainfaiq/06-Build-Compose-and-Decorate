class Student:
    def __init__(self, name, marks):
        # Using self to initialize instance attributes
        self.name = name
        self.marks = marks

    def display(self):
        # Using self to access and print instance attributes
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
# Create an instance of Student
student = Student("Hussain", 85)

# Call the display method to show student details
student.display()
