from experta import *

# Define a class named EmergencyFund that inherits from the Fact class
class EmergencyFund(Fact):
    # Define a field named emergency_fund of type int, which is mandatory for the fact to be valid
    emergency_fund = Field(int, mandatory=True)
    expenses = Field(int, mandatory=True)
