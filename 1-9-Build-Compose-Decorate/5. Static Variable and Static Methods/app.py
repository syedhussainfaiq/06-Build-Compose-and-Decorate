class MathUtils:
    # Static method to add two number

    @staticmethod
    def add (a , b) :
        return a + b
    


# using the static method without creating an instance
result = MathUtils.add(10, 20)

# print the result
print("The sum is", result)
        