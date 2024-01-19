from experta import KnowledgeEngine, Rule, MATCH

from facts.CreditCard import CreditCard
from facts.EmergencyFund import EmergencyFund
from facts.Expenses import Expenses
from facts.Income import Income
from facts.RetirementSavings import RetirementSavings
from facts.Savings import Savings


class FinancialAdvice(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.advice = []

    def reset(self):
        super().reset()
        self.advice = []

    def accumulate_advice(self, message):
        self.advice.append(message)

    # Rule for evaluating credit card debt
    @Rule(CreditCard(credit_card_debt=MATCH.credit_card_debt, income=MATCH.income))
    def credit_card_rule(self, credit_card_debt, income):
        result_message = ""
        # If credit card debt is greater than income
        if credit_card_debt > income:
            result_message = "You should really try to pay off your credit card debt (${0}). Having a CC debt greater than your income (${1}) is generally not a good idea.".format(credit_card_debt, income)

        # If credit card debt is between 0 and income
        elif 0 < credit_card_debt < income:
            result_message = "It isn't bad to have CC debt (${0}), continue to try to manage this.".format(credit_card_debt)

        # If credit card debt is 0
        elif credit_card_debt == 0:
            result_message = "Great job. You have (${0}) CC debt. You may want to consider looking into rewards based CC's.".format(credit_card_debt)

        # If credit card debt is negative (they owe you money)
        else:
            result_message = "If this is true, you are doing a great job managing your credit card debt (${0}). They actually owe you money! KEEP IT UP!!!".format(credit_card_debt)
        
        self.accumulate_advice(result_message)

    # Rule for evaluating emergency fund
    @Rule(EmergencyFund(emergency_fund=MATCH.emergency_fund, expenses=MATCH.expenses))
    def emergency_fund_rule(self, emergency_fund, expenses):
        result_message = ""
        # If emergency fund is 0
        if emergency_fund == 0:
            result_message = "You should start to build an emergency fund in case something unexpected happens."

        # If emergency fund is equal to expenses
        elif emergency_fund == expenses:
            result_message = "You have an emergency fund equal to your expenses. You should really consider increasing your emergency fund."

        # If emergency fund is between 0 and 6 times expenses
        elif 0 < emergency_fund < expenses * 6:
            result_message = "Good job setting some money aside in case of an emergency. You should increase the amount to at least ${0} which is your expenses ${1} * 6.".format(expenses * 6, expenses)

        # If emergency fund is between 6 times expenses and 12 times expenses
        elif expenses * 6 < emergency_fund < expenses * 12:
            result_message = "You are doing a wonderful job with your emergency fund (${0})! Keep it up! Maybe set a goal to get to 12 months expenses saved up (${1})?!?".format(emergency_fund, expenses * 12)

        # If emergency fund is greater than 12 times expenses
        elif emergency_fund > expenses * 12:
            result_message = "You are doing a terrific job managing your emergency fund (${0}). KEEP IT UP!!!".format(emergency_fund)

        # If emergency fund is negative
        else:
            result_message = "This shouldn't be possible. But it seems that you have a negative emergency fund (${0}). You should really start to build an emergency fund in case something unexpected happens.".format(emergency_fund)
        self.accumulate_advice(result_message)

    # Rule for evaluating expenses
    @Rule(Expenses(expenses=MATCH.expenses, income=MATCH.income))
    def expenses_rule(self, expenses, income):
        result_message = ""
        # If expenses are 0 (no expenses)
        if expenses == 0:
            result_message = "WOW!! That is pretty impressive that you have (${0}) in expenses.".format(expenses)

        # If expenses are greater than income (they are spending more than they make)
        elif expenses >= income:
            result_message = "You don't make enough money (${0}) to accommodate your expenses (${1}), cut down on the expenses.".format(income, expenses)

        # If expenses are less than 1/3 of income
        elif expenses < (income / 3):
            result_message = "Keep up the good work! Your expenses of ${0} are less than 1/3 of your income ${1}.".format(expenses, round((income / 3), 2))

        # If expenses are greater than 1/3 of income but less than income
        elif income > expenses > (income / 3):
            result_message = "You should cut back on your expenses (${0}). Ideally the max expenses should be no more than 1/3 of your income (${1}).".format(expenses, round((income / 3), 2))

        # If expenses are negative
        else:
            result_message = "You are doing a great job managing your expenses (${0}). Looks like you are making money off from your expenses. Seems a little odd.".format(expenses)

        self.accumulate_advice(result_message)
        
    # Rule for evaluating income
    @Rule(Income(income=MATCH.income))
    def income_rule(self, income):

        result_message = ""

        # If income is 0
        if income == 0:
            result_message = "You should really get a job..."

        # If income is between 0 and 4000
        elif 0 < income < 4000:
            result_message = "You could definitely do better, I recommend looking into either furthering your education or looking for a better job. You are currently making ${0} a month.".format(income)

        # If income is between 4000 and 8000
        elif 4000 < income < 8000:
            result_message = "You are doing pretty good. Keep it up!! You are currently making ${0} a month.".format(income)

        # If income is greater than 8000
        elif income >= 8000:
            result_message = "WOW! Good for you! You are bringing in quite a bit of money! You are currently making ${0} a month.".format(income)

        # If income is not a number or less than 0
        else:
            result_message = "Sorry, that wasn't a number. Since you can't follow direction, I presume you aren't making much money. You are currently making ${0} a month.".format(income)

        self.accumulate_advice(result_message)

    # Rule for evaluating savings account
    @Rule(Savings(savings_account=MATCH.savings_account, income=MATCH.income))
    def savings_rule(self, savings_account, income):

        result_message = ""

        # If savings account is 0
        if savings_account == 0:
            result_message = "You should really open a savings account."

        # If income is greater than savings account and savings account is greater than 0
        elif income > savings_account > 0:
            result_message = "Your monthly income ${0} is higher than what you have in savings. You should probably be putting away more money. You have ${1} in your savings account.".format(income, savings_account)

        # If income is less than savings account
        elif income < savings_account:
            result_message = "Your monthly income ${0} is lower than what you have in savings. You are doing an ok job putting away money. You have ${1} in your savings account.".format(income, savings_account)

        elif income == savings_account:
            result_message = "Your monthly income ${0} is equal to what you have in savings ${1}. You should probably be putting away more money.".format(income, savings_account)

        # If income is less than savings account but less than 3 times income
        elif income < savings_account < income * 3:
            result_message = "You are doing a good job with your savings. Is there anyway you could add more? You have ${0} in your savings account.".format(savings_account)

        # If savings account is greater than 3 times income
        elif savings_account > income * 3:
            result_message = "You are doing a great job with your savings. KEEP IT UP!!! You have ${0} in your savings account.".format(savings_account)
        # If savings account is not meeting any criteria, provide benchmarks
        else:
            result_message = "Unfortunately there is no way to evaluate your savings account at this time."

        self.accumulate_advice(result_message)

    # Rule for evaluating retirement savings
    @Rule(RetirementSavings(retirement_savings=MATCH.retirement_savings, age=MATCH.age, salary=MATCH.salary))
    def retirement_savings_rule(self, retirement_savings, age, salary):

        result_message = ""
        retirementSavingsByForty = salary * 3
        retirementSavingsByFifty = salary * 6
        retirementSavingsBySixty = salary * 8
        retirementSavingsBySixtySeven = salary * 10

        # If retirement savings is 0
        if retirement_savings == 0:
            result_message = "Have you started saving for retirement? You should really start to save for retirement."

        # If retirement savings is less than salary and age is between 20 and 30
        elif retirement_savings < salary and 20 < age < 30:
            result_message = "You aren't doing a bad job with your retirement savings (${0}), but I recommend getting your savings to match your salary (${1}) by the time you hit 30.".format(retirement_savings, salary)

        # If retirement savings is less than retirement savings by forty and age is between 30 and 40
        elif retirement_savings < retirementSavingsByForty and 30 <= age < 40:
            result_message = "You aren't doing a bad job with your retirement savings (${0}). I recommend that by the time you hit 40 you have at least ${1} in your retirement account.".format(retirement_savings , retirementSavingsByForty)

        # If retirement savings is less than retirement savings by fifty and age is between 40 and 50
        elif retirement_savings < retirementSavingsByFifty and 40 <= age <= 50:
            result_message = "You aren't doing a bad job with your retirement savings (${0}). I recommend that by the time you hit 50 you have at least ${1} in your retirement account.".format(retirement_savings, retirementSavingsByFifty)

        # If retirement savings is less than retirement savings by sixty and age is between 50 and 60
        elif retirement_savings < retirementSavingsBySixty and 50 <= age <= 60:
            result_message = "You aren't doing a bad job with your retirement savings (${0}). I recommend that by the time you hit 60 you have at least ${1} in your retirement account.".format(retirement_savings, retirementSavingsBySixty)

        # If retirement savings is less than retirement savings by sixtyseven and age is between 60 and 67
        elif retirement_savings < retirementSavingsBySixtySeven and 60 <= age <= 67:
            result_message = "You aren't doing a bad job with your retirement savings (${0}). I recommend that by the time you hit 67 you have at least ${1} in your retirement account.".format(retirement_savings, retirementSavingsBySixtySeven)

        # If retirement savings is greater than or equal to retirement savings by sixtyseven and age is 67 or greater
        elif retirement_savings >= retirementSavingsBySixtySeven and 67 <= age:
            result_message = "Looks like you are just about set to retire! Good for you!! Retirement Savings = ${0}".format(retirement_savings)

        # If retirement savings is not meeting any criteria, provide benchmarks
        else:
            result_message = "You are doing a great job managing your retirement savings.\n" \
                             "Here are the benchmarks to make sure you are hitting:\n" \
                             "Age 30: Retirement Savings = ${0}\n" \
                             "Age 40: Retirement Savings = ${1}\n" \
                             "Age 50: Retirement Savings = ${2}\n" \
                             "Age 60: Retirement Savings = ${3}\n" \
                             "Age 67: Retirement Savings = ${4}\n".format(salary, retirementSavingsByForty, retirementSavingsByFifty,
                                                                         retirementSavingsBySixty, retirementSavingsBySixtySeven)

        
        self.accumulate_advice(result_message)
