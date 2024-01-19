from experta import *


# Define a class called 'RetirementSavings' that inherits from the 'Fact' class.
class RetirementSavings(Fact):
    # Create a field named 'retirement_savings' of type 'int' to store the retirement savings amount.
    # This field is marked as mandatory, indicating that it must be provided when creating an instance of the class.
    retirement_savings = Field(int, mandatory=True)

    # Create a field named 'age' of type 'int' to store the person's age.
    # This field is marked as mandatory, indicating that it must be provided when creating an instance of the class.
    age = Field(int, mandatory=True)

    # Create a field named 'salary' of type 'int' to store the person's salary.
    # This field is marked as mandatory, indicating that it must be provided when creating an instance of the class.
    salary = Field(int, mandatory=True)
