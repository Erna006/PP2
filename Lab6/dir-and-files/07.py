f = open(r"C:\Users\ernad\Desktop\PP2\Lab6\dir-and-files\text.txt", "r")
new = open(r"C:\Users\ernad\Desktop\PP2\Lab6\dir-and-files\to_copy.txt", "w")
for line in f:
    new.write(line)