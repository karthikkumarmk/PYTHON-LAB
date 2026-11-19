class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


# Creating an object
account = BankAccount("Karthik", 7000)

account.deposit(3000)
account.withdraw(4000)
account.display()