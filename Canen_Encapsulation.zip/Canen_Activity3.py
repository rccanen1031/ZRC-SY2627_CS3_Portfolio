class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = 0
        self.set_balance(balance)

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("The balance must be not be a negative number.")

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return {self.__balance:.2}

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance



print("Object of class BankAccount")
my_account = BankAccount(12345, 1000)

print("Output:")
print("Account 1")
print("Account Number:", my_account.account_number)
print("Balance:", my_account.balance)

print("\nUpdate balance to -100")
my_account.set_balance(-100)

print("Account Number:", my_account.account_number)
print("Balance:", my_account.balance)