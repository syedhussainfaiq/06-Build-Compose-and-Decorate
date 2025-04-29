class Person:
    def __init__(self, name):
        self.name = name # Initalize the name field
        print(f"Person constructor called for {self.name}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name) # Call the base class constructor
        self.subject = subject # Initialize the subject field
        print(f"Teacher constructor called for {self.name}, subject: {self.subject}")



# Example usage
if __name__ == "__main__":
    teacher = Teacher("Fariz Hussain", "English")
    print(f"Name: {teacher.name}, Subject: {teacher.subject}")        


