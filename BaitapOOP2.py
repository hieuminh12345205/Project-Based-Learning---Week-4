class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance
    
    @property
    def account_number(self):
        return self.__account_number
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Nạp tiền thành công: {amount}. Số dư mới: {self.__balance}")
        else:
            print("Số tiền nạp phải lớn hơn 0")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Rút tiền thành công: {amount}. Số dư mới: {self.__balance}")
        elif amount > self.__balance:
            print("Số dư không đủ để rút tiền")
        else:
            print("Số tiền rút phải lớn hơn 0")
    
    def get_balance(self):
        return self.__balance


# Sử dụng
account = BankAccount("1234567890", 1000)
print(f"Số tài khoản: {account.account_number}")
print(f"Số dư ban đầu: {account.get_balance()}")

account.deposit(500)
account.withdraw(300)
account.withdraw(5000)
print(f"Số dư cuối cùng: {account.get_balance()}")