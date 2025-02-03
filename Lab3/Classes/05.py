"""Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals,
and test to make sure the account can't be overdrawn."""
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, sum):
        if sum > 0:
            self.balance += sum
        else:
            print("Deposit sum must be more than 0")
    def withdraw(self, sumout):
        if sumout <= self.balance:
            self.balance -= sumout
        else:
            print("Withdrawal amount can not be more than in deposit")
    def __str__(self):
        return f"Owner: {self.owner}\nBalance: {self.balance}"

user1 = Account("Someone", 10000)
user1.deposit(100)
user1.withdraw(9000)
print(user1)