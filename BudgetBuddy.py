'''
As a university student, I noticed that keeping track of expenses can be tedious and 
overwhelming for many students. To make this easier, I created BudgetBuddy: a simple 
command-line tool to help you manage your personal finances effortlessly!

This program will help the user with:
    1. Setting a monthly budget.
    2. Adding transactions.
    3. Checking your current balance and seeing if you’ve exceeded your budget.
    4. Generating a summary of your finances and saving it locally.
'''

# Color codes for terminal output
RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'

# 1 - Printing welcome message for the user.
print(BLUE + 'Welcome to BudgetBuddy, your personal finance tracker!\n' + RESET)

# 2 - This function adds a transaction to the list of transactions.
def add_transaction(transaction, amount, description):
    transaction.append((amount, description))

# 3 - This function calculates the balance remaining from the transactions and monthly_budget.
def calculate_balance(transaction, monthly_budget):
    total_expense = sum(amount for amount, _ in transaction)
    balance = monthly_budget - total_expense
    return balance

# 4 - This function checks if the budget is exceeded.
def budget_exceeded(transaction, monthly_budget):
    return calculate_balance(transaction, monthly_budget) < 0

# 5 - This function gets the summary of all the transactions and the balance.
def get_summary(transaction, monthly_budget, month):
    summary = []
    summary.append('Month: ' + month + '\n')
    summary.append('Budget for the month: $' + str(monthly_budget) + '\n')
    summary.append('\nTransactions:\n')

    for amount, description in transaction:
        summary.append('• $' + str(amount) + ' - ' + description + '\n')

    summary.append('\nBalance: $' + str(calculate_balance(transaction, monthly_budget)) + '\n')

    # Add plain message for use in both file and terminal
    if budget_exceeded(transaction, monthly_budget):
        summary.append('You have exceeded your budget.\n')
    else:
        summary.append('You are within your budget.\n')

    return summary

# 6 - This function saves the summary to an output file.
def save_summary(summary, file):
    with open(file, 'w') as out:
        for line in summary:
            out.write(line)

# 7 - This is the main function that controls the flow of the program.
def main():
    transaction = []
    monthly_budget = float(input(BLUE + 'Please enter your budget for this month: $' + RESET))
    month = input(BLUE + 'Enter the month you are tracking: ' + RESET)

    while True:
        print(YELLOW + '\nWhat would you like to do?' + RESET)
        print('1. Add a transaction')
        print('2. Check your balance')
        print('3. View summary')
        print('4. Save summary')
        print('5. Exit\n')

        try:
            choice = int(input(BLUE + 'Enter your choice (1-5): ' + RESET))
        except ValueError:
            print(RED + 'Invalid input. Please enter a number between 1 and 5.\n' + RESET)
            continue

        if choice == 1:
            try:
                amount = float(input('Enter the transaction amount: $'))
                description = input('Enter the transaction description: ')
                add_transaction(transaction, amount, description)
                print(GREEN + 'Transaction added successfully!\n' + RESET)
            except ValueError:
                print(RED + 'Invalid amount entered. Please try again.\n' + RESET)

        elif choice == 2:
            balance = calculate_balance(transaction, monthly_budget)
            print(YELLOW + f'Your current balance is: ${balance:.2f}\n' + RESET)

        elif choice == 3:
            summary = get_summary(transaction, monthly_budget, month)
            for line in summary[:-1]:
                print(line, end='')

            # Print the final budget status with color
            if budget_exceeded(transaction, monthly_budget):
                print(RED + summary[-1] + RESET)
            else:
                print(GREEN + summary[-1] + RESET)

        elif choice == 4:
            summary = get_summary(transaction, monthly_budget, month)
            save_summary(summary, 'output.txt')
            print(GREEN + 'Summary saved successfully to output.txt!\n' + RESET)

        elif choice == 5:
            print(BLUE + 'Thank you for using BudgetBuddy!\n' + RESET)
            break

        else:
            print(RED + 'Error! Invalid choice entered.\n' + RESET)

main()
