# Bank application with minimum balance condition

MIN_BALANCE = 1000  # minimum balance that must remain in the account

# Accept customer name and initial balance
name = input("Enter customer name: ")
balance = float(input("Enter initial account balance: "))

# Accept deposit amount and update the balance
deposit = float(input("Enter amount to deposit: "))
balance = balance + deposit

# Accept withdrawal amount
withdraw = float(input("Enter amount to withdraw: "))

# Allow withdrawal only if the remaining balance stays >= 1000
if balance - withdraw >= MIN_BALANCE:
    balance = balance - withdraw      # withdrawal allowed
else:
    print("Withdrawal denied! Balance cannot fall below", MIN_BALANCE)

# Display the updated balance
print("Customer Name:", name)
print("Updated Account Balance:", balance)