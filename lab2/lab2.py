#Python Boolean
print(10 > 9) #Output: True
print(10 == 9) #Output: False
print(10 < 9) #Output: False

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #Output:b is not greater than a
  
def myFunction():
  return True
print(myFunction()) #Output: True

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")#Output: YES!

#Python Operators
a = 10
b = 3
print("Addition:", a + b) # Output: 13
print("Subtraction:", a - b) # Output: 7
print("Multiplication:", a * b) # Output: 30
print("Division:", a / b) # Output: 3.3333...
print("Floor Division:", a // b) # Output: 3
print("Modulus:", a % b) # Output: 1
print("Exponentiation:", a ** b) # Output: 1000

print("Is a equal to b?", a == b) # Output: False
print("Is a not equal to b?", a != b) # Output: True
print("Is a greater than b?", a > b) # Output: True
print("Is a less than or equal to b?", a <= b) # Output: False

x = True
y = False
print("x and y:", x and y) # Output: False
print("x or y:", x or y) # Output: True
print("not x:", not x) # Output: False

#Python Lists (Features: Ordered, Changeable, Allow Dublicates)
thislist = ["apple", "banana", "cherry"]
print(thislist) # Output: ['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) # Output: ['apple', 'banana', 'cherry', 'apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # Output: 3

mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # Output: <class 'list'>

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # Output: apple

fruits.append("orange")
print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.remove("banana")
print(fruits) # Output: ['apple', 'cherry', 'orange']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) #[23, 50, 65, 82, 100]

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # [100, 82, 65, 50, 23]

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) # ["apple", "banana", "cherry"]

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) # ['a', 'b', 'c', 1, 2, 3]
for x in list2:
  list1.append(x)
print(list1) # ['a', 'b', 'c', 1, 2, 3]
list1.extend(list2)
print(list1) # ['a', 'b', 'c', 1, 2, 3]

#Tuple (Features: Ordered, UNCHANGEABLE, Allow Dublicates)
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) # ('apple', 'banana', 'cherry', 'apple', 'cherry')

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Sets (Features: UNORDERED, UNCHANGEABLE, DON'T ALLOW DUBLICATES)
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)# {'banana', 'cherry', 'apple'}

unique_numbers = {1, 2, 3, 4, 4, 5}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
unique_numbers.add(6)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}

#Dictionary (Features: Ordered, Changeable, DON'T ALLOW DUBLICATES)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)#{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#If...Else

a = 33
b = 200
if b > a:
  print("b is greater than a")#b is greater than a
  
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")#a and b are equal
  
a = 200
b = 33
if b > a:
  print("b is greater than a")#b is greater than a
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")#b is not greater than a
  
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")#Both conditions are True
  
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")#Nested Condition

a = 33
b = 200
if b > a:
  pass

#While Loop
i = 1
while i < 6:
  print(i)
  i += 1 # 1 2 3 4 5
  
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 # 1 2 3
  
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) #1 2 4 5 6
  
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")# 1 2 3 4 5 i is no longer less than 6
  
#For Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) #apple banana cherry
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break # apple banana
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) #apple
  
for x in range(6):
  print(x) #0 1 2 3 4 5

for x in range(2, 6):
  print(x) #2 3 4 5
  
for x in range(2, 30, 3):
  print(x)#2 5 8 11 14 17 20 23 26 29
  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) #red apple red banana red cherry big apple big banana big cherry tasty apple tasty banana tasty cherry

