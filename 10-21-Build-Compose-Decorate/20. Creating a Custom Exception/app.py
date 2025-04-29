# Define the custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18"):
        self.message = message
        super().__init__(self.message)

# Define the function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18.")
    print(f"Age {age} is valid.")

# Test the function with try...except
try:
    user_age = 16  # Example: an invalid age
    check_age(user_age)
except InvalidAgeError as e:
    print(f"Error: {e}")
else:
    print("Age is acceptable.")
finally:
    print("Age check completed.")
