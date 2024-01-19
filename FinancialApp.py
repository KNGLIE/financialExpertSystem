import tkinter as tk
from tkinter import messagebox
 
from engine.FinancialAdvice import FinancialAdvice
from facts.CreditCard import CreditCard
from facts.EmergencyFund import EmergencyFund
from facts.Expenses import Expenses
from facts.Income import Income
from facts.RetirementSavings import RetirementSavings
from facts.Savings import Savings


# Class to create the GUI for the financial expert system
class FinancialApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Financial Expert System")
        self.geometry("950x650")

        # Create the input fields
        self.income_label = tk.Label(self, text="Monthly Income:")
        self.income_entry = tk.Entry(self)

        self.expenses_label = tk.Label(self, text="Monthly Expenses:")
        self.expenses_entry = tk.Entry(self)

        self.credit_card_label = tk.Label(self, text="Credit Card Debt:")
        self.credit_card_entry = tk.Entry(self)

        self.savings_label = tk.Label(self, text="Savings Account:")
        self.savings_entry = tk.Entry(self)

        self.retirement_savings_label = tk.Label(self, text="Retirement Savings:")
        self.retirement_savings_entry = tk.Entry(self)

        self.age_label = tk.Label(self, text="Your Age:")
        self.age_entry = tk.Entry(self)

        self.emergency_fund_label = tk.Label(self, text="Emergency Fund:")
        self.emergency_fund_entry = tk.Entry(self)

        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_financial_advice)

        # Label to display advice
        self.advice_label = tk.Label(self, text="Financial Advice:")
        self.advice_label.grid(row=8, columnspan=2, pady=5) 

        # Layout
        self.income_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.income_entry.grid(row=0, column=1, padx=5, pady=5)

        self.expenses_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.expenses_entry.grid(row=1, column=1, padx=5, pady=5)

        self.credit_card_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.credit_card_entry.grid(row=2, column=1, padx=5, pady=5)

        self.savings_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.savings_entry.grid(row=3, column=1, padx=5, pady=5)

        self.retirement_savings_label.grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.retirement_savings_entry.grid(row=4, column=1, padx=5, pady=5)

        self.age_label.grid(row=5, column=0, sticky="e", padx=5, pady=5)
        self.age_entry.grid(row=5, column=1, padx=5, pady=5)

        self.emergency_fund_label.grid(row=6, column=0, sticky="e", padx=5, pady=5)
        self.emergency_fund_entry.grid(row=6, column=1, padx=5, pady=5)

        self.calculate_button.grid(row=7, columnspan=2, pady=10)

    # Method to calculate the financial advice based on the provided input
    def calculate_financial_advice(self):
        try:
            # Get the input values from the entry fields
            income = int(self.income_entry.get())
            expenses = int(self.expenses_entry.get())
            credit_card_debt = int(self.credit_card_entry.get())
            savings_account = int(self.savings_entry.get())
            retirement_savings = int(self.retirement_savings_entry.get())
            age = int(self.age_entry.get())
            emergency_fund = int(self.emergency_fund_entry.get())

            # Create the facts based on the provided input
            engine = FinancialAdvice()
            engine.reset()

            income_fact = Income(income=income)
            engine.declare(income_fact)

            expenses_fact = Expenses(expenses=expenses, income=income)
            engine.declare(expenses_fact)

            retirement_savings_fact = RetirementSavings(retirement_savings=retirement_savings, age=age, salary=income * 12)
            engine.declare(retirement_savings_fact)

            credit_card_fact = CreditCard(credit_card_debt=credit_card_debt, income=income)
            engine.declare(credit_card_fact)

            savings_fact = Savings(savings_account=savings_account, income=income)
            engine.declare(savings_fact)

            emergency_fund_fact = EmergencyFund(emergency_fund=emergency_fund, expenses=expenses)
            engine.declare(emergency_fund_fact)

            engine.run()

            # Check if all the input values are valid
            if not all(entry.isdigit() for entry in [self.income_entry.get(), self.expenses_entry.get(), self.credit_card_entry.get(), self.savings_entry.get(), self.retirement_savings_entry.get(), self.age_entry.get(), self.emergency_fund_entry.get()]):
                raise ValueError("Invalid input. Please enter valid numerical values in all fields.")

            # Run the engine to calculate the financial advice based on the provided input
            advice_messages = engine.advice 
            self.display_advice(advice_messages)

        except ValueError as e:
            import traceback
            traceback.print_exc()
            messagebox.showerror("Input Error", f"{e}")

    # Method to display the financial advice
    def display_advice(self, advice_messages):
        if advice_messages:
            advice_text = "\n".join(advice_messages)
            self.advice_label.config(text=f"Financial Advice:\n{advice_text}")
        else:
            self.advice_label.config(text="No financial advice available.")


if __name__ == "__main__":
    app = FinancialApp()
    app.title("Financial Advice Simple Expert System(Please take this advice with a grain of salt.)")
    app.mainloop()
