def add():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    print(a+b)
def sub():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    print(a-b)
def div():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    print(a/b)
def mul():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    print(a*b)
d="y"
while d=="y":
    print('''
            1=addition
            2=substraction
            3=multiplicaton
            4=division''')
    c=int(input("enter the operation"))
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        mul()
    elif c==4:
        div()
    else:
     print("invalid operator")
    # print("do u want to continue y/n")
    d=input("do u want to continue y/n")           
# while a or b ==0:
      

