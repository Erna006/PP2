#                                                        Booleans
print(10 > 9)   #True
print(10 == 9)  #False
print(10 < 9)   #False


print(bool("Hello")) #True
print(bool(15)) #True
bool("abc") #True
bool(123) #True
bool(["apple", "cherry", "banana"]) #True


bool(False) #False
bool(None) #False
bool(0) #False
bool("") #False
bool(()) #False
bool([]) #False
bool({}) #False


#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


#Check if an object is an integer or not:
x = 200
print(isinstance(x, int))