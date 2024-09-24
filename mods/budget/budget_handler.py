"""
logic for budget
"""
from data_handler.variables.constants import *


class Budget:

    def __init__(self):
        self.monthly_income = 0
        self.expenses = []  # stores dictionary {expense_category: 'entertainment' , expenses: []}
        self.expense_budget_category = [(ESSENTIAL_EXPENSES,
                                         [HOUSING, UTILITIES, GROCERIES, TRANSPORTATION, INSURANCE,
                                          HEALTHCARE, DEBT_PAYMENTS]),
                                        (NON_ESSENTIAL_EXPENSES,
                                         [DINING_OUT, ENTERTAINMENT, PERSONAL_CARE, CLOTHING, EDUCATION,
                                          HOBBIES_AND_LEISURE, TRAVEL_VACATIONS, GIFTS_DONATIONS]),
                                        (SAVINGS_AND_INVESTMENTS,
                                         [EMERGENCY_FUND, RETIREMENT_SAVINGS, INVESTMENTS, EDUCATION_SAVINGS,
                                          MAJOR_PURCHASES])]

        self.budgets = []  # dictionary that hold goals; {budget_name: 'Fast Food', goal_budget: 200}
        self.budget_alerts = []  # pulls budgets and saves them as a dictionary with current expenses(budget_name:
        # 'fastfood', current_expenses": []}
        self.current_debt = []  # {debt_name: 'credit card', total_debt: 3000}
        self.total_debt = 0
        self.assets = 0
        self.checking_balance = 0
        self.savings_balance = 0
        self.credit_card_balances = []
        self.credit_card_limits = []
        self.net_worth = 0

    def expense(self, expense_category: str, expense_type: str, expense_total: float):
        if expense_category == ESSENTIAL_EXPENSES:
            pass
        elif expense_category == NON_ESSENTIAL_EXPENSES:
            pass
        elif expense_category == SAVINGS_AND_INVESTMENTS:
            pass
        else:
            print('Please select a valid expense category.')

    def add_remove_credit_info(self):
        pass

    def add_remove_budget(self, budget_name, budget_total):
        self.budgets.append({'budget_name': budget_name, 'budget_total': budget_total})

    def budget_alerter(self, budget_name, ):
        """
        needs to take in current budget name and check to see what the budget total is set at. then needs to scan all
        expenses that match that budget name. needs to return a percentage of used budget. and how many $$ the use has
        left to spend in that category. Try and set up a time frame setting

        """
        pass

    def add_remove_debt(self, debt_name, debt_total, add_or_remove):  # add date
        """Adds or removes deb from debt list."""
        if add_or_remove == ADD:
            self.current_debt.append({'debt_name': debt_name, 'debt_total': debt_total})
        elif add_or_remove == REMOVE:
            self.current_debt.remove(debt_name) if debt_name in self.current_debt else print('Debt not found.')
        else:
            print('Please enter a valid choice.')

    def debt_handler(self):
        """
        This mau need to be under the user section to add differnt menues to it.

        """
        pass

    def net_savings(self):
        #Net Savings = Income – Expenses
        pass

    def savings_rate(self):
        #Savings Rate (%) = (Savings ÷ Income) × 100
        pass

    def debt_to_income_ratio(self):
        #Debt-to-Income Ratio (%) = (Debt Payments ÷ Income) × 100
        pass

    def fifty_thirty_twenty_rule(self):
        """
        Needs = 0.5 × Income
        Wants = 0.3 × Income
        Savings = 0.2 × Income

        50/30/20 Rule
A popular budgeting guideline:

50% Needs (Fixed expenses like housing, groceries, insurance)
30% Wants (Entertainment, dining, non-essentials)
20% Savings/Debt repayment

        """
        pass

    def emergency_fund_calculator(self):
        # Emergency Fund = 3-6 × Monthly Expenses
        pass

    def sinking_fund_contribution(self):
        #Sinking Fund Contribution = Goal ÷ Time
        #look this up
        pass

    def compound_interest_calculator(self):
        #Compound Interest (for savings goals) = P(1 + r/n)^(nt)
        pass

    def cash_flow_forcasting(self):
        #Cash Flow Forecasting = Current Savings + (Monthly Surplus × Number of Months)
        pass

    def dislpay_current_budget_breakdown(self):
        import matplotlib.pyplot as plt

        # Pie chart data
        labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
        sizes = [15, 30, 45, 10]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

        # Create a pie chart
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    def debt_to_income(self, total_monthly_debt_payments, gross_monthly_income):
        return (total_monthly_debt_payments / gross_monthly_income) * 100

    # Debt-to-Asset Ratio
    def debt_to_asset(self, total_debt, total_assets):
        return (self.total_debt / self.assets) * 100

    # Consumer Debt-to-Income Ratio
    def consumer_debt_to_income(self, consumer_debt, gross_annual_income):
        return (consumer_debt / gross_annual_income) * 100

    # Loan-to-Value (LTV) Ratio
    def loan_to_value(self, loan_amount, appraised_value_of_asset):
        return (loan_amount / appraised_value_of_asset) * 100

    # Credit Utilization Ratio
    def credit_utilization(self, total_credit_card_balances, total_credit_limits):
        return (total_credit_card_balances / total_credit_limits) * 100

    # Savings-to-Debt Ratio
    def savings_to_debt(self, total_savings, total_debt):
        return (total_savings / total_debt) * 100

    # Emergency Fund Ratio
    def emergency_fund_ratio(self, total_emergency_savings, monthly_expenses):
        return total_emergency_savings / monthly_expenses

    # Mortgage-to-Income Ratio
    def mortgage_to_income(self, monthly_mortgage_payment, gross_monthly_income):
        return (monthly_mortgage_payment / gross_monthly_income) * 100

    # Personal Debt-to-Net Worth Ratio
    def debt_to_net_worth(self, total_debt, net_worth):
        return (total_debt / net_worth) * 100

    # Debt Repayment Ratio
    def debt_repayment_ratio(self, annual_debt_payments, gross_annual_income):
        return (annual_debt_payments / gross_annual_income) * 100
