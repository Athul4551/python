num=[]
c=[]
n=int(input("enter a list range"))
for i in range(n):
    z=int(input())
    num.append(z)
print(num)
# b=num
# print(b)
v=int(input("enter a target"))
m=len(num)
# print(m)
for i in range(m):
    for j in range(m):
        t=num[i]+num[j]
        if t==v:
            if i in c and j in c:
                pass
            else:
                print(i,j)
                c.append(j)    
                c.append(i)      
    


