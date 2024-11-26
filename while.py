n=int(input("enter a number"))
e=n
s=0
d=0
while n>0:
    s=n%10
    d=d*10+s
    n=n//10
print(d)    
# if(e==d):
#     print("is palindrom")
# else:
#     print("not palindrom")       

