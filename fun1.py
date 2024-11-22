list1=[1,2,3,4,5,6,7,8,9]
even1=[]
odd2=[]
def even(list1):
    for i in list1:
        if i%2==0: 
            even1.append(i)
    return even1        
def odd(list1):
    for i in list1:
        if i%2==1:
            odd2.append(i)
    return  odd2
print(even(list1))
print(odd(list1))        
        
    