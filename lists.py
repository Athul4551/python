# a=["apple",1,"orang",[2,3,5,6]]
# for i in a:
#     print(i)
# a=["apple",1,"orang",[2,3,5,6]]
# b=len(a)
# a='orange'
# b=len(a)
# for i in range(b):
#     print(a[i])
a=["apple",1,"orang",[2,3,5,6],"f",5,6]
print(a[:3])
a[1]="grape"
print(a[0:])
a[1:3]=4,2,"mango"
print(a[0:])