from experta import Fact, Field

# Define a class named "Savings" that inherits from the "Fact" class
class Savings(Fact):
    # Define a field named "savings_account" of type int, which is mandatory
    savings_account = Field(int, mandatory=True)
    # Define a field named "income" of type int, which is mandatory
    income = Field(int, mandatory=True)
