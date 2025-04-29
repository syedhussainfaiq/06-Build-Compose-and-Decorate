class Logger:
    def __init__(self):
        # Constructor: called when the object is created
        print("Logger object created.")

    def __del__(self):
        # Destructor: called when the object is destroyed
        print("Logger object destroyed.")

# Example usage
print("Creating Logger instance:")
logger = Logger()

print("\nDeleting Logger instance:")
del logger  # Explicitly deleting the object

print("\nEnd of program.")
