class BankAccount:

    def __init__(self, account_holder, balance):
        if balance < 0:
            raise ValueError("balance cannot be negative")
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposit Amount cannot be Negative")

        self.__balance += amount
        print("Amount Deposit Successfully")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        
        self.__balance -= amount
        print("Amount Withdrow Successfully")

    def get_balance(self):
        return self.__balance

    def show_account_details(self):
        print(f"Name :{self.account_holder}")
        print(f"Balance :{self.__balance}")

My_Account = BankAccount("Danish", 50000)

My_Account.show_account_details()

My_Account.withdraw(60000)

print(My_Account.get_balance())