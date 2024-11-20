am={"name":"athul","age":20,"name":"anit","elec":False}
# print(am)
# print(am["name"])
# print(len(am))
# print(type(am))
# am=dict(nmae="athul",age=20)
print(am)
x=am["name"]
print(x)
a=am.get("name")
print(a)
s=am.keys()
print(s)
d=am.values()
print(d)
g=am.items()
print(g)
if "name" in am:
    print("yes")
am["name"]="athul"
print(am)
am.update({"age":21})
print(am)
am.update({"color":"red"})
print(am) 
am["num"]=1
print(am)   
