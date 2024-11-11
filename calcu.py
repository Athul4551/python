d="y"
while d=="y":
    a=int(input("enter first number"))
    b=int(input("enter first number"))
    print('''
            1=addition
            2=substraction
            3=multiplicaton
            4=division''')
    c=int(input("enter the operation"))
    if c==1:
        s=a+b
        print("sum=",s)
    elif c==2:
        s=a-b
        print("sub=",s)
    elif c==3:
        s=a*b
        print("mul=",s)
    elif c==4:
        s=a/b
        print("div=",s)
    else:
        print("invalid operator")
    # print("do u want to continue y/n")
    d=input("do u want to continue y/n")    
           
            
# while a or b ==0:
    
    
