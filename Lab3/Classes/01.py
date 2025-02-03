# Define a class which has at least two methods: getString: to get a string from console input 
# printString: to print the string in upper case.
class Myclass:
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())

n = Myclass()
n.getString()
n.printString()