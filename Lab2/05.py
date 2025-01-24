#                                           Python Sets
# Set items are unordered, unchangeable, and do not allow duplicate values.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)                      # {'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}
print(len(thisset))                 # 3

myset = {"apple", "banana", "cherry"}
print(type(myset))                  # <class 'set'>

#           Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}


#           Access Set Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)          # True
print("banana" not in thisset)      # False


#           Add Set Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)                      # {'orange', 'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)                      # {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)                      # {'banana', 'cherry', 'apple', 'orange', 'kiwi'}


#           Remove Set Items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)                      # {'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)                      # {'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()  # Remove a random item
print(x)                            # apple
print(thisset)                      # {'cherry', 'banana'}

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)                      # set()


#           Join Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)                         # {3, 'c', 2, 'b', 1, 'a'}
# You can use the | operator instead of the union() method, and you will get the same result.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)                        # {apple, cherry, 'a', John, Elena, 3, 'c', banana, 2, 'b', 1}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)                        # {banana, cherry, John, 'b', Elena, 2, 1, apple, 3, 'c', 'a'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)                         # {'apple'}
# You can use the & operator instead of the intersection() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)                         # {'banana', 'cherry'}
# You can use the - operator instead of the difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)                         # {'google', 'banana', 'microsoft', 'cherry'}
# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.


#           Set Methods
# add()	 	                                Adds an element to the set
# clear()	                	            Removes all the elements from the set
# copy()	 	                            Returns a copy of the set
# difference()	 	                   -    Returns a set containing the difference between two or more sets
# difference_update()	  	          -=    Removes the items in this set that are also included in another, specified set
# discard()	 	                            Remove the specified item
# intersection()	 	               &    Returns a set, that is the intersection of two other sets
# intersection_update()	  	          &=    Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	                        Returns whether two sets have a intersection or not
# issubset()	  	                  <=    Returns whether another set contains this set or not
#  	 	                               <    Returns whether all items in this set is present in other, specified set(s)
# issuperset()	  	                  >=    Returns whether this set contains another set or not
#  	 	                               >    Returns whether all items in other, specified set(s) is present in this set
# pop()	 	                                Removes an element from the set
# remove()	                                Removes the specified element
# symmetric_difference()    	       ^    Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	  	  ^=    Inserts the symmetric differences from this set and another
# union()	   	                       |    Return a set containing the union of sets
# update()	  	                      |=    Update the set with the union of this set and others