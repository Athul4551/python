# try:
#     print('hello')
# except:
#     print("An excepction occurd")
# else:
#     print("nothing")
# finally:
#     print("complated")        
# x=-1
# if x<0:
#     raise ZeroDivisinError("sorry no number below  zero")
# x=1
# try:
#     print(x)
#     raise ZeroDivisionError
# except NameError:
#     print("variable x is not define")
# except:
#     print("somthing else want wrong")
x=4
y=2
try:
    z=x/y
except ZeroDivisionError:
    z=x
print(z)        