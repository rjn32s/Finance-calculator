"""
Contains all of the functions.
Here is the list of function

"""

def lumpsum_calculator(invested_amount, rate_of_return, tenure):
    future_value = [invested_amount * (1 + rate_of_return/100)**year for year in range(1, int(tenure+1))]
    return future_value


def calculate_sip(amount, rate_of_return, tenure, investment_frequency):
    if investment_frequency == "monthly":
        investment_period = tenure * 12
        monthly_investment = amount
        annual_rate_of_return = rate_of_return / 100

        # Calculate the future value of investments
        future_value = 0
        for i in range(investment_period):
            future_value += monthly_investment
            future_value *= (1 + annual_rate_of_return / 12)

    elif investment_frequency == "yearly":
        investment_period = tenure
        yearly_investment = amount
        annual_rate_of_return = rate_of_return / 100

        # Calculate the future value of investments
        future_value = 0
        for i in range(investment_period):
            future_value += yearly_investment
            future_value *= (1 + annual_rate_of_return)

    else:
        return "Invalid investment frequency. Please choose 'monthly' or 'yearly'."

    return future_value


def calculate_lumpsum(target_wealth, rate_of_return, tenure, adjust_inflation=False):
    target_value = target_wealth
    annual_rate_of_return = rate_of_return / 100
    investment_period = tenure

    if adjust_inflation:
        # Adjust for inflation
        inflation_rate = 3 / 100  # Assuming 3% inflation rate
        target_value /= (1 + inflation_rate) ** investment_period

    # Calculate the required lumpsum investment
    investment_amount = target_value / (1 + annual_rate_of_return) ** investment_period

    return investment_amount



def calculate_regular_investment(investment_frequency, target_wealth, rate_of_return, tenure, adjust_inflation=False):
    if investment_frequency == "monthly":
        investment_period = tenure * 12
        investment_amount = target_wealth / (((1 + rate_of_return / 100) ** (1 / 12)) ** investment_period)

    elif investment_frequency == "yearly":
        investment_period = tenure
        investment_amount = target_wealth / ((1 + rate_of_return / 100) ** investment_period)

    else:
        return "Invalid investment frequency. Please choose 'monthly' or 'yearly'."

    if adjust_inflation:
        inflation_rate = 3 / 100  # Assuming 3% inflation rate
        investment_amount /= (1 + inflation_rate) ** investment_period

    return investment_amount



def calculate_time_duration(target_wealth, investment_amount, rate_of_return):
    target_value = target_wealth
    annual_rate_of_return = rate_of_return / 100

    # Calculate the time duration
    time_duration = 0
    while investment_amount < target_value:
        investment_amount *= (1 + annual_rate_of_return)
        time_duration += 1

    return time_duration



def calculate_sip_time_duration(investment_frequency, target_wealth, investment_amount, rate_of_return):
    if investment_frequency == "monthly":
        monthly_investment = investment_amount
        annual_rate_of_return = rate_of_return / 100

        # Calculate the time duration
        time_duration = 0
        current_wealth = 0
        while current_wealth < target_wealth:
            current_wealth += monthly_investment
            current_wealth *= (1 + annual_rate_of_return / 12)
            time_duration += 1

    elif investment_frequency == "yearly":
        yearly_investment = investment_amount
        annual_rate_of_return = rate_of_return / 100

        # Calculate the time duration
        time_duration = 0
        current_wealth = 0
        while current_wealth < target_wealth:
            current_wealth += yearly_investment
            current_wealth *= (1 + annual_rate_of_return)
            time_duration += 1

    else:
        return "Invalid investment frequency. Please choose 'monthly' or 'yearly'."

    return time_duration


def calculate_retirement_investment(current_age, retirement_age, life_expectancy, rate_of_return, current_expense):
    years_to_retirement = retirement_age - current_age
    years_in_retirement = life_expectancy - retirement_age
    annual_rate_of_return = rate_of_return / 100

    # Calculate the required investment amount
    investment_amount = current_expense * (1 - (1 + annual_rate_of_return) ** -years_in_retirement) / annual_rate_of_return

    return investment_amount


def calculate_equity_investment_percentage(current_salary, current_age, monthly_savings_percentage):
    monthly_savings = current_salary * (monthly_savings_percentage / 100)

    # Calculate the equity investment amount
    equity_investment_amount = monthly_savings * (65 - current_age)

    return equity_investment_amount


import matplotlib.pyplot as plt

def calculate_returns_fd_vs_equity(investment_amount, tenure):
    annual_fd_interest_rate = 6  # Fixed Deposit interest rate
    annual_equity_returns = 10  # Equity investment returns

    # Calculate FD returns
    fd_returns = investment_amount * (1 + annual_fd_interest_rate / 100) ** tenure - investment_amount

    # Calculate equity investment returns
    equity_returns = investment_amount * (1 + annual_equity_returns / 100) ** tenure - investment_amount

    # Plotting the returns
    years = list(range(1, tenure + 1))
    fd_returns_data = [investment_amount * (1 + annual_fd_interest_rate / 100) ** year - investment_amount for year in years]
    equity_returns_data = [investment_amount * (1 + annual_equity_returns / 100) ** year - investment_amount for year in years]

    plt.plot(years, fd_returns_data, label='Fixed Deposit Returns')
    plt.plot(years, equity_returns_data, label='Equity Investment Returns')
    plt.xlabel('Tenure (in years)')
    plt.ylabel('Returns')
    plt.title('FD vs Equity Returns')
    plt.legend()
    plt.show()

    return fd_returns, equity_returns


def calculate_step_up_returns(monthly_investment_amount, investment_growth_rate, rate_of_return, tenure):
    annual_growth_rate = investment_growth_rate / 100
    annual_rate_of_return = rate_of_return / 100

    # Calculate the returns with step-up investment
    total_returns = 0
    current_investment = monthly_investment_amount
    for year in range(1, tenure + 1):
        total_returns += current_investment * (1 + annual_rate_of_return) ** year
        current_investment += current_investment * annual_growth_rate

    return total_returns


def calculate_emi(loan_amount, loan_tenure, interest_rate):
    months = loan_tenure * 12
    monthly_interest_rate = interest_rate / 100 / 12

    # Calculate the monthly EMI
    emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** months) / ((1 + monthly_interest_rate) ** months - 1)

    return emi

def calculate_gst_amount(amount, gst_percentage, gst_inclusive=True):
    if gst_inclusive:
        gst_amount = (amount * gst_percentage) / (100 + gst_percentage)
    else:
        gst_amount = (amount * gst_percentage) / 100

    return gst_amount
