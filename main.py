from facts.CreditCard import CreditCard
from facts.Expenses import Expenses
from facts.EmergencyFund import EmergencyFund
from engine.FinancialAdvice import FinancialAdvice
from facts.Income import Income
from facts.RetirementSavings import RetirementSavings
from facts.Savings import Savings


def main():
    # Create an instance of the FinancialAdvice engine
    engine = FinancialAdvice()
    
    # Reset the engine to remove any existing facts
    engine.reset()

    # Prompt the user for input and store the values in variables
    income = int(input("What is your monthly income?\n"))
    credit_card_debt = int(input("How much credit card debt do you have?\n"))
    expenses_value = int(input("What are your monthly expenses?\n"))
    savings_account = int(input("How much money do you have in your savings account?\n"))
    retirement_savings = int(input("How much do you have in your retirement savings account?\n"))
    age = int(input("How old are you?\n"))
    emergency_fund = int(input("How much do you have in your emergency fund?\n"))

    # Create instances of the relevant fact classes and provide the values from user input
    income_fact = Income(income=income)
    engine.declare(income_fact)

    expenses_fact = Expenses(expenses=expenses_value, income=income)
    engine.declare(expenses_fact)

    retirement_savings_fact = RetirementSavings(retirement_savings=retirement_savings, age=age, salary=income * 12)
    engine.declare(retirement_savings_fact)

    credit_card_fact = CreditCard(credit_card_debt=credit_card_debt, income=income)
    engine.declare(credit_card_fact)

    savings_fact = Savings(savings_account=savings_account, income=income)
    engine.declare(savings_fact)

    emergency_fund_fact = EmergencyFund(emergency_fund=emergency_fund, expenses=expenses_value)
    engine.declare(emergency_fund_fact)

    # Run the engine to calculate the financial advice based on the provided input
    engine.run()


if __name__ == '__main__':
    main()
