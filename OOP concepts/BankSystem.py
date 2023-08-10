
# def __init__(self, b):
#         self.bal = b
bal = 1000
def withdraw( amount):  
        if amount <= bal:   
            bal = bal - amount
            print("Withdraw amount {} successful . . . !".format(amount))
            print("Remaining Balance: " + str(bal)) 
            
        else:
            print("You don't have enough balance . . .!")
            
def deposit( amount):  
        bal = bal + amount
        print("Deposit amount {} successful . . . !".format(amount))
        print("Your current balance: " + str(bal))  
        
# p1 = BankSystem(1000)

def hello():
      print("hello")
# p1.withdraw(100)  
