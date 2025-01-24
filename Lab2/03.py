#                              Python Lists
#           Python Lists
thislist = ["apple", "banana", "cherry"]    # ['apple', 'banana', 'cherry']
print(thislist)

thislist = ["apple", "banana", "cherry"]    # 3
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]      # <class 'list'>
print(type(mylist))


#           Access List Items
thislist = ["apple", "banana", "cherry"]    # banana
print(thislist[1])

thislist = ["apple", "banana", "cherry"]    # cherry
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])                        # ['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])                         # ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])                         # ['cherry', 'orange', 'kiwi', 'melon', 'mango']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])                      # ['orange', 'kiwi', 'melon']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[::2])                        # ['apple', 'cherry', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


#           Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)                             # ['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)                             # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)                             # ['apple', 'blackcurrant', 'watermelon', 'cherry']


#           Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)                             # ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)                             # ['apple', 'orange', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)                             # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


#           Remove List Items
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)                             # ['apple', 'cherry', 'banana', 'kiwi']

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)                             # ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)                             # ['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)                             # ['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)                             # this will cause an error because you have succsesfully deleted "thislist".

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)                             # []


#           Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)                                  # Print all items in the list, one by one

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])                        # Print all items by referring to their index number

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])                        # Print all items, using a while loop to go through all the index numbers
  i += 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]                # A short hand for loop that will print all items in a list


#           List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)                              # ['apple', 'banana', 'mango']
# Same:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)

# The Syntax
#newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]               # ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in range(10)]            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x.upper() for x in fruits]       # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

newlist = ['hello' for x in fruits]         # ['hello', 'hello', 'hello', 'hello', 'hello']

newlist = [x if x != "banana" else "orange" for x in fruits]  # ['apple', 'orange', 'cherry', 'kiwi', 'mango']


#           Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)                             # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)                             # [23, 50, 65, 82, 100]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)                             # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)                             # [100, 82, 65, 50, 23]

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)                             # [50, 65, 23, 82, 100]

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)                             # ['banana', 'cherry', 'Kiwi', 'Orange']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)                             # ['cherry', 'Kiwi', 'Orange', 'banana']


#           Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)                               # ['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)                               # ['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)                               # ['apple', 'banana', 'cherry']


#           Join Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)                                # ['a', 'b', 'c', 1, 2, 3]


#           List Methods     
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list