#list
#data=[1,2,3,4,5]
data=["a","b","c","d","e"]
a=[1,2,3,4]
data.append("g")# to add last element of g
print(data)
#data.extend("a")# to add last element of a
data.insert(2,a)# to add element of 2 position
#data.clear()#to clear all elements
data2=data.copy()# to copy all data
print(data2)
#print(type(data))
#print(dir(data))
print(data.count("b"))# to count of numbers in list
print(data.index("d"))# to find index of number

'''
pop
remove
reverse
sort
'''
#pop# to remove last element in the list and print it agian
list=[25,67,77]
print(list)
print(list.pop())
#remove # to remove all elements from the list
list=[25,67,77]
print(list)
print(list.remove(67))
print(list)
#reverse # to reverse all elements from the list
list=["a","h","f"]
list.reverse()
print(list)
#sort # to sort all elements in assending order
list=["a","h","u","t","n"]
list.sort()
print(list)
prime_number=[11,7,3,5,2,]
prime_number.sort()
print(prime_number)