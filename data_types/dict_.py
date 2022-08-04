data={"name":"sai","age":22,"college":"svc","DOB":"1998-06-11"}
data2={"list":("sai","bhanu",123,4),"age":22,"college":"svc","DOB":"1998-06-11"}
data3={"tuple":("sai","bhanu",123,4),"age":22,"college":"svc","DOB":"1998-06-11"}
print(data)
print(data2)
print(data3)
'''
print(type(data))
print(type(data2))
print(type(data3))
print(dir(data))
print(data.get("DOB"))
print(data["DOB"])
print(data.keys())
print(data.values())
print(data.items())
data.update(data2)
data.setdefault("sal",25000)
print("15-->",data)
'''
#print(data.has_key("age")) (error accored)
print(len(data))
print("name" in data)