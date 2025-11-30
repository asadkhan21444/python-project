class balanecException(Exception):
    pass

class  BankAccount:
    def __init__(self, initialAmount, accName ):
        self.balance = initialAmount
        self.name = accName

        print(f"\nAccount created for  {self.name} with initial balance: {self.balance}" )

    def getBalance(self):
        print(f"\nAccount {self.name} balance = ${self.balance  }")


    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\n Deposit Complete.\nAccount {self.name} balance = ${self.balance  }")

    def vaibleTranction(self, amount):
        if self.balance >= amount:
            return 
    def vaibleTranction(self, amount):
        if self.balance >= amount:
            return
        raise balanecException(
                f"\n Sorry , account {self.name} only  has a balance of ${self.balance}"
            )
        raise balanecException(
                f"\n Sorry , account {self.name} only  has a balance of ${self.balance}"
            )

    def new_method(self, amount):
        return self.balance - amount
        
    def withdraw(self,amount):
        try:
            self.vaibleTranction(amount)
            self.balance = self.balance - amount
            print("\n withdraw complete")
            self.getBalance()

        except balanecException as error:
            print(f"\n withdraw interuped:{error}") 



    def transfer(self, amount,  account):
        try:
            print(f"\n*****************\n\nBeginning transfer.. ")
            self.vaibleTranction(amount)
            self.withdraw(amount)
            self.deposit(amount)
            print("\nTranfer Complete!\n\n******************")
        except balanecException as error:
            print(f'/n Transfer interruped . {error} ')


class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount + 1.05)
        