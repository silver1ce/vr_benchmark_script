import pandas as pd

def create_budget(income, expenses):
    #Create a budget based on income and expenses
    budget = income - expenses
    return budget

def calculate_net_worth(assets, liabilities):
    #Calculate your net worth based on your assets and liabilities
    net_worth = assets - liabilities
    return net_worth

def create_spending_report(transactions):
    #Create a spending report based on transaction data
    # Convert transaction data into a Pandas dataframe
    df = pd.DataFrame(transactions, columns=['date', 'description', 'amount'])
    # Group transactions by month and calculate the total spent each month
    df['date'] = pd.to_datetime(df['date']) # Convert date column to datetime format
    monthly_spending = df.groupby(pd.Grouper(key='date', freq='M'))['amount'].sum().reset_index()
    return monthly_spending


income = int(input("what is your monthly income : "))
expenses = int(input("what is your monthly expenses : ")) # fixed expenses
budget = create_budget(income, expenses)
print("Your budget is: € ", budget)

assets = int(input("what is your total assets : "))
liabilities = int(input("what is your total liabilities : "))
net_worth = calculate_net_worth(assets, liabilities)
print("Your net worth is: € ", net_worth)

transactions = []

while True:
    date = input("Enter transaction date (yyyy-mm-dd), or type 'done' if finished: ")
    if date == 'done':
        break
    description = input("Enter transaction description: ")
    amount = int(input("Enter transaction amount (positive for income, negative for expenses): "))
    transactions.append((date, description, amount))
    


# transactions(example) = [('2023-01-01', 'Vaate Kauppa', -50),
#                 ('2023-01-05', 'Bensa', -30),
#                 ('2023-01-15', 'matka', -400),
#                 ('2023-02-01', 'Ravintola', -75),
#                 ('2023-02-10', 'Elokuva', -20),
#                 ('2023-03-03', 'Bensa', -45),
#                 ('2023-03-16', 'Osake Kauppa', -600)]
spending_report = create_spending_report(transactions)

print(f"Your extra expenses is \n{spending_report}")




    

