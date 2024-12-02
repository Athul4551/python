class book():
    def __init__(self,author,book_name,copy):
        self.author=author
        self.book_name=book_name
        self.copy=copy
        self.year=year
    def  purchase(self,bo):
        print(bo)
        d=int(input("enter book sl no"))
        co1=5
        co2=2
        co3=3
        if d==1 and co1>0:
            co1=co1-1
            print("thanku")
        elif d==2 and co2>0:
             co2=co2-1
            print("thanku")
        elif d==3 and co3>0:
            co3=co3-1
            print("thanku")   
        else:
            print("exit") 
        # self.copy=self.copy-1
    def returnbook(self):
        print(bo)
        d=int(input("enter book sl no"))
        if d==1 and co1>0:
            co1=co1+1
            print("thanku")
        elif d==2 and co2>0:
             co2=co2+1
            print("thanku")
        elif d==3 and co3>0:
            co3=co3+1
            print("thanku")   
        else:
            print("exit") 
        # self.copy=self.copy+1
    def addbook(self):
        name=input("enter the book name")
        s=int(input("how many copys are availabile"))
        au=input("who is the author")
        bo.append(name)
bo=[1"1984",2"To kill a mockingbird",3"Great Gatsby"]        
d="y"
while d=="y":
    print('''1,purchase
             2,return
             3,add book''')
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
        
        
    