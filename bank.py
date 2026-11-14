# Bank application: basic account operations

# Accept customer name and initial balance
name = input("Enter customer name: ")
balance = float(input("Enter initial account balance: "))

# Accept deposit amount and update the balance
deposit = float(input("Enter amount to deposit: "))
balance = balance + deposit

# Accept withdrawal amount and update the balance
withdraw = float(input("Enter amount to withdraw: "))
balance = balance - withdraw

# Display the updated balance
print("Customer Name:", name)
print("Updated Account Balance:", balance)