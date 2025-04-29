class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        # Return the iterator object (usually self)
        return self

    def __next__(self):
        # Logic to define the next item in the iteration
        if self.current < 0:
            raise StopIteration  # Signal that the iteration is complete
        value = self.current
        self.current -= 1
        return value

# Example usage
countdown = Countdown(5)

# Iterating using a for-loop
print("Countdown:")
for number in countdown:
    print(number)
