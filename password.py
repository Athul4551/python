import re
print('''Minimum length of 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character''')
s=input("enter the password")
a=len(s)
# print(a)
if re.findall("[a-zA-Z]",s)==True:
    if re.findall("\d",s)==True:
        if re.findall("[!@#$%^&*()_]",s)==True:
            if a>8:
                print("powerfull password")
else:
    print("week password")                
            