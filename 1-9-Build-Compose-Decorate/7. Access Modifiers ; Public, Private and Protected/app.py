class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name # Public variable
        self._salary = salary # Protected variable
        self.__ssn = ssn   # Private variable


    def get_private_ssn(self):
     """Public method to access the private variable."""
     return self.__ssn


# Testing access modifiers

if __name__ == "__main__":
    emp = Employee("Hussain", 50000, "123-45-6789")


    # Accessing the public variable
    print(f"Public variable - Name: {emp.name}") # Work fine

    # Accessing the protected variable
    print(f"Protected variable - salary: {emp._salary} ") # Work but should be accessed with caution

    # Accessing the private variable
    try:
     print(f"Private variable - SSN: {emp.__ssn}") # This will raise an AttributError

    except AttributeError as e:
     print(f"Error accessing private variable directly: {e}")

   # Accesssing the private variable using a public method
    print(f"Private variable (via method) - SSN: {emp.get_private_ssn()}")  


    