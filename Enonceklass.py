class BankAccount:
  
   def __init__(self, idaccount_number, account_holder, initial_balance):
      if initial_balance < 500.00 :
         print("kont inisyal ou dwe depase 500 goud")

      self.idaccount_number = idaccount_number
      self.account_holder = account_holder
      self.initial_balance = initial_balance

   def deposit(self,amount):
    self.initial_balance = self.initial_balance + amount
      

   def withdraw(self,amount):
        self.initial_balance = self.initial_balance - amount
      
   def get_balance(self):
        return self.initial_balance

   def __str__ (self):
          return "Account number : {} \n Account Holder : {}\n balance : {} HTG".format(self.idaccount_number,self.account_holder,self.initial_balance)

account1 = BankAccount("123456","king bob",10000)
account1.deposit(500.00)
account1.withdraw(200.00)
balance = account1.get_balance()
print("\t\t-----Account 1 :------\n",account1)

account2 = BankAccount("678942","king Ragnar",23000)
account2.deposit(13000)
account2.withdraw(2000)
balance = account2.get_balance()
print("\t\t-----Account 2 :------\n",account2)

account3 = BankAccount("652891","Ivar the Bornless",18000)
account3.deposit(14000)
account3.withdraw(5000)
balance = account3.get_balance()
print("\t\t-----Account 3 :------\n",account3)

account4 = BankAccount("652844","Bjorn Cote de fer",19000)
account4.deposit(14000)
account4.withdraw(5000)
balance = account4.get_balance()
print("\t\t-----Account 4 :------\n",account4)


         
        
    

