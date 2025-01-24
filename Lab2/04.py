#                                         Python Tuples 
# A tuple is a collection which is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)                            # ("apple", "banana", "cherry")

print(len(thistuple))                       # 3

thistuple = ("apple",)
print(type(thistuple))                      # <class 'tuple'>

thistuple = ("apple")
print(type(thistuple))                      # <class 'str'>

#Date Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

#           Access Tuple Items
# Same as the list


#           Update Tuples
""" Tuples are unchangeable, meaning that you cannot change, add, or remove items 
once the tuple is created.But there is a workaround. You can convert the tuple into 
a list, change the list, and convert the list back into a tuple """

# Convert the tuple into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)

#           Unpack Tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)                                # apple
print(yellow)                               # banana
print(red)                                  # cherry

# Using Asterisk "*"
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)                                # apple
print(yellow)                               # banana
print(red)                                  # ['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)                                # apple
print(tropic)                               # ['mango', 'papaya', 'pineapple']
print(red)                                  # cherry


#           Loop Tuples
# Same as the list


#           Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)                               # ('a', 'b', 'c', 1, 2, 3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)                              # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


#           Tuple Methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found