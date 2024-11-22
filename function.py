def add(*x):
    print(x[0]+x[1])
def sub(**x):
    print(x["a"]-x["b"])
def div(a,b):
    return(a/b)
def mul(a,b):
    print(a*b)
d="y"
a=int(input("enter a number"))
b=int(input("enter a number"))
while d=="y":
    print('''
            1=addition
            2=substraction
            3=multiplicaton
            4=division''')
    c=int(input("enter the operation"))
    if c==1:
        add(a,b)
    elif c==2:
        sub(a=a,b=b)
    elif c==3:
        mul(a,b)
    elif c==4:
       print(div(a,b))
    else:
     print("invalid operator")
    # print("do u want to continue y/n")
    d=input("do u want to continue y/n")           
# while a or b ==0:
      

