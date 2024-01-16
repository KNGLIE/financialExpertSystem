from experta import Fact, Field

# Define a class named CreditCard that inherits from Fact
class CreditCard(Fact):
    # Define a field named credit_card_debt with type int, and set it as mandatory
    credit_card_debt = Field(int, mandatory=True)
    # Define a field named income with type int, and set it as mandatory
    income = Field(int, mandatory=True)
