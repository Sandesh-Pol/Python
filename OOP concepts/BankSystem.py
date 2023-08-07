class BankSystem:
    def __init__(self, b):
        self.bal = b
        
    def withdraw(self, amount):  
        if amount <= self.bal:   
            self.bal = self.bal - amount
            print("Withdraw amount {} successful . . . !".format(amount))
            print("Remaining Balance: " + str(self.bal)) 
            
        else:
            print("You don't have enough balance . . .!")
            
    def deposit(self, amount):  
        self.bal = self.bal + amount
        print("Deposit amount {} successful . . . !".format(amount))
        print("Your current balance: " + str(self.bal))  
        
p1 = BankSystem(1000)

p1.withdraw(100)  
