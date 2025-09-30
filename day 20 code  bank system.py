# Day 20 - Basic Bank Account System
# Author: Momina Raheel
# Description: A simple Python program to simulate a basic bank account.
# Features: deposit, withdraw, check balance.

class BankAccount:
    # Constructor to initialize account with owner's name and balance
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposit Successful! {amount} added.")
        else:
            print("❌ Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds! Withdrawal not possible.")
        elif amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"✅ Withdrawal Successful! {amount} deducted.")

    # Method to check balance
    def check_balance(self):
        print(f"💰 Current Balance: {self.balance}")


# ---------- Program Execution ----------
print("🏦 Welcome to the Basic Bank Account System")

# Create an account for the user
name = input("Enter your name: ")
account = BankAccount(name)

# Menu-driven program
while True:
    print("\nWhat would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("👋 Thank you for using the system. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1 and 4.")
