class Bank:
    
    def __init__(self,balance):
        self.balance=balance
    def deposit(self):
        b=int(input('enter the deposit amound'))
        self.balance=self.balance+b 
    def withdrawl(self):
        b=int(input('enter the withdrawl amound'))
        self.balance=self.balance-b
    def check(self):
        print(self.balance)    
bank1=Bank(0)
d="y"
while d=="y":
    print('''1.deposit
            2.withdrawl
            3.check balance''')
    c=int(input("enter the option number"))
    if c==1:
        bank1.deposit()
    elif c==2:
        bank1.withdrawl()
    elif c==3:
        bank1.check()   
    else:
        print("exit") 
    d=input("do u want continu y/n")          
    
    
