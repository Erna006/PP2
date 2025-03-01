f = open(r"C:\Users\ernad\Desktop\PP2\Lab6\dir-and-files\text.txt", "w")
list = [1, 2, 3, 4, 6, 4, 7, 3]
for i in range(len(list)):
    if i == 0:
        f.write("[")
    if i != len(list) - 1:
        f.write(f"{str(list[i])}, ")
    if i == len(list) - 1:
        f.write(f"{str(list[i])}]")
f.close()