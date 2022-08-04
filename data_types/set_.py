#set
data={1,2,3,4,5}
#print(type(data))
#print(data)
#data.add(7)
#data.clear()
#data2=data.copy()
#print(data2)
#print(data)
# difference comparision between 2 set and we can not print duplicates

fruits={"apple","banana","mango"}
company={"google","facebook","apple"}
#cmp=fruits.difference(company)
#cmp=company.difference(fruits)

#print(cmp) comparision between 2 set and we cannot print duplicates and print onlly one set

#fruits.difference_update(company)
#company.difference_update(fruits)
#print(fruits)

#discard to remove selected elements

#data5={"apple","banana","mango"}
#print(data5)
#data5.discard("banana")
#print(data5)
#intersection to print same elements in two sets
common=fruits.intersection(company)
print(common)
print(fruits&company)
print(dir(data))
#union to print without duplicates in two sets
union_data=fruits.union(company)
print(union_data)
print(fruits|company)

fruits1={"apple","banana","mango"}
company1={"google","facebook","apple"}
fruits1.update(company1)
print(fruits1)
fruits1.pop()# on order data types to print valves

print(fruits1)
#difference we can use - symbol and duplicates are not allowed to print
#symmetric we can use ^ symbol and print continue order in two sets