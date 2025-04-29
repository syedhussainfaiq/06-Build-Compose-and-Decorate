class A:
    def show(self):
        print("A's show() method")

class B(A):
    def show(self):
        print("B's show() method")

class C(A):
    def show(self):
        print("C's show() method")

class D(B, C):
    pass

# Create an object of class D and call show()
d = D()
d.show()

# Print the MRO of class D
print("\nMethod Resolution Order (MRO):")
print(D.mro())
