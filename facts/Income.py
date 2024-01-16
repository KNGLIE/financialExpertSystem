from experta import * 

 # Defining a class called 'Income' which inherits from 'Fact' class
class Income(Fact): 
    # Creating a field called 'income' of type integer with mandatory flag set to True
    income = Field(int, mandatory=True)  
