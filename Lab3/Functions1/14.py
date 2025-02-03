f = open("C:\\Users\\ernad\\Desktop\\PP2\\Lab3\\Functions1\\14_1.txt", "r+")
n = open("C:\\Users\\ernad\\Desktop\\PP2\\Lab3\\Functions1\\11.py", "r")
infile = n.read()

f.write(infile)
f.seek(0)
print(f.read())

f.close()
n.close()