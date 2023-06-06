# Write a Python class called BankAccount with methods for depositing, withdrawing,
# and checking the account balance.

class BankAccount:
    def __init__(self, money: int, account_num: str, key_num: str) -> None:
        self.money = money
        self.account_num = account_num
        self.key_num = key_num
        pass

    def depositing(self, more_money:int):
        self.money += more_money
        print (f"¡You're depositing ${more_money} was success!")
        self.account_balance()

    def withdrawing(self, get_money:int, account_num: str, key_num: str ):
        if account_num == self.account_num and key_num == self.key_num and get_money < self.money:
            self.money -= get_money
            print (f'¡Your withdraw was success! Take your cash ${get_money}')
            self.account_balance()
        print(f'Insuffient Money.')

    def account_balance(self):
        print( '**********  ACCOUNT BALANCE  ***********')
        print( f'Your account balance is: ${self.money} ')
        print( '**********  ***************  ***********')


person1 = BankAccount(3000000, '123456', 'abcd')
person2 = BankAccount(100000, '654321', 'asdf')

print('***Person 1: ')
person1.account_balance
person1.depositing(10000)
person1.withdrawing(1800000,'123456', 'abcd')
person1.account_balance
print('***Person 2: ')
person2.withdrawing(50000, '654321', 'asdf')
person2.withdrawing(30000, '654321', 'asdf')
person2.depositing(1000)
person2.withdrawing(30000, '654321', 'asdf')
        
        