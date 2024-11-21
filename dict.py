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
# am.pop("color")
# print(am)
# am.popitem()
# print(am)
del am["color"]
print(am)
# del am
# print(am)
# am.clear()
# print(am)
# ma=am.copy()
# print(ma)
# mmm=dict(ma)
# print(mmm)
child1={"name":"athul","email":"ashusgwhys5@"}
child2={"name":"akash","email":"ahgvfxv3fvxv4v4@"}
# print(arr)
# print(arr["child2"]["name"])
zz={"child1":child1,"child2":child2}
print(zz)