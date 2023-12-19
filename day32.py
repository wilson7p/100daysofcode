#Implement a class for a bank account with methods for deposit and withdrawal.
print ("\nWilson - Day 32 of #100DaysOfCode\n") 
print("\na bank account with methods for deposit and withdrawal.")

class BankAccount:
  def __init__(self, account_holder, balance = 0):
    self.account_holder = account_holder
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"deposit of ${amount} successful. new balance: ${self.balance}")
    else:
      print("enter positive number")

  def withdraw(self, amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      print(f"withdraw of ${amount} successfull. new balance: ${self.balance}")
    else:
      print("enter positive number")  

  def get_balance(self):
    return self.balance

account_holder_name = input("enter account_holder_name: ")
initial_balance = int(input("enter initial_balance: "))
account = BankAccount(account_holder_name, initial_balance)

while True:
  print("\n1. deposit\n2. withdraw\n3. check balance\n4.exit")
  choice = input("enter ur choice: ")

  if choice == "1":
    deposit_amount = int(input("deposit amount: "))
    choice = input("enter ur choice: ")

  elif choice == "2":
    withdraw_amount = int(input("withdraw amount: "))
    account.withdraw(withdraw_amount)

  elif choice == "3":
    print(f"current balance: ${account.get_balance()}")
  
  elif choice == "4":
    break

  else:
    print("enter between 1-4")
