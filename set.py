# b={1,2,3}
# print(b)
s={12,3,4,68,89,1,9}
# print(s)
# for i in s:
#     print(i)
# print(2 in s)
# if 3 in s:
#     print("2 is present")
# else:   
#     print()
# a=len(s)
# print(a)    
# s.add(6)
# print(s)
# s.update([13,14,15])
# print(s)
# s.remove(12)
# print(s)
# s.discard(68)
# print(s)
# s.clear()
# print(s)
# del(s)
# print(s)
a=[12,3,4,68,89,1,9]
b=set(a)
print(b)
b.pop()
print(b)
m={13,78,98,6,9,7}
# c=s.union(m)
# print(c)
c=s.intersection(m)
print(c)
c=s.difference(m)
print(c)