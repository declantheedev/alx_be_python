monthly_income = int(input('Enter your monthly income:'));
total_monthly_expenses = int(input('Enter your total monthly expenses:'));
monthly_savings = monthly_income - total_monthly_expenses;
annual_interest = 0.05;
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest);
print('Your monthly savings are: {}'.format(monthly_savings));
print('Projected savings after one year, with interest is: {}'.format(projected_savings));