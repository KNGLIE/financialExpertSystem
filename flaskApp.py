from flask import Flask, render_template, request, redirect, url_for, flash, session

from engine.FinancialAdvice import FinancialAdvice
from facts.CreditCard import CreditCard
from facts.EmergencyFund import EmergencyFund
from facts.Expenses import Expenses
from facts.Income import Income
from facts.RetirementSavings import RetirementSavings
from facts.Savings import Savings

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'advice_messages' not in session:
        session['advice_messages'] = []

    if request.method == 'POST':
        try:
            # Get the input values from the form
            income = int(request.form['income'])
            expenses = int(request.form['expenses'])
            credit_card_debt = int(request.form['credit_card'])
            savings_account = int(request.form['savings'])
            retirement_savings = int(request.form['retirement_savings'])
            age = int(request.form['age'])
            emergency_fund = int(request.form['emergency_fund'])

            # Create the facts based on the provided input
            engine = FinancialAdvice()
            engine.reset()

            income_fact = Income(income=income)
            engine.declare(income_fact)

            expenses_fact = Expenses(expenses=expenses, income=income)
            engine.declare(expenses_fact)

            retirement_savings_fact = RetirementSavings(retirement_savings=retirement_savings, age=age,
                                                        salary=income * 12)
            engine.declare(retirement_savings_fact)

            credit_card_fact = CreditCard(credit_card_debt=credit_card_debt, income=income)
            engine.declare(credit_card_fact)

            savings_fact = Savings(savings_account=savings_account, income=income)
            engine.declare(savings_fact)

            emergency_fund_fact = EmergencyFund(emergency_fund=emergency_fund, expenses=expenses)
            engine.declare(emergency_fund_fact)

            engine.run()

            # Check if all the input values are valid
            if not all(str(entry).isdigit() for entry in
                       [income, expenses, credit_card_debt, savings_account, retirement_savings, age, emergency_fund]):
                raise ValueError("Invalid input. Please enter valid numerical values in all fields.")

            # Run the engine to calculate the financial advice based on the provided input
            advice_messages = engine.advice

            # Update session with the new advice_messages
            session['advice_messages'] = advice_messages

            # Redirect to results without passing advice_messages in URL
            return redirect(url_for('results'))

        except ValueError as e:
            flash(f"Input Error: {e}")

    return render_template('index.html', advice_messages=session['advice_messages'])


@app.route('/results', methods=['GET'])
def results():
    # Retrieve advice_messages from session
    advice_messages = session.pop('advice_messages', [])
    return render_template('results.html', advice_messages=advice_messages)


if __name__ == "__main__":
    app.run(debug=True)
