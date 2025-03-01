f = open(r'C:\Users\ernad\Desktop\PP2\Lab6\dir-and-files\text.txt', 'r')
count = 0
for i in f:
    count += 1
print(count)
f.close()