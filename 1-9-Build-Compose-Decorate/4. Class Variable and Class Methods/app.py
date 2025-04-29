class Bank:
  # Class Variable
  bank_name = "Global Bank"

  # class method to chang bank name
  @classmethod
  def chang_bank_name(cls, name):
    cls.bank_name = name

# Create instance of the Bank class
# 
branch1 = Bank()
branch2 = Bank()

# show initial bank name for both instant
print("Initial Bank Name (branch1)", branch1.bank_name ) 
print("Initial Bank Name (branch2)", branch2.bank_name )

# Chang the bank name using class method
Bank.chang_bank_name("Fasial Bank")

# Show update bank name for both instances
print("Update Bank Name (branch1)", branch1.bank_name)
print("Update Bank Name (branch2)", branch2.bank_name)