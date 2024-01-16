from experta import *

# Define a Fact class named Expenses
class Expenses(Fact):
    # Define a field named 'expenses' of type int
    expenses = Field(int, mandatory=True)
    # Define a field named 'income' of type int
    income = Field(int, mandatory=True)
