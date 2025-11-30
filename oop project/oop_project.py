from bank_Account import *

asad = BankAccount(10000, "asad")
khan = BankAccount(20000, "khan")

asad.getBalance()
khan.getBalance()

asad.deposit(500)

khan.withdraw(288)

khan.transfer(122222,asad)
# khan.transfer(122,asad)