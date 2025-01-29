"""You are given list of numbers separated by spaces.
Write a function filter_prime which will take list of numbers as an
agrument and returns only prime numbers from the list."""
# №1
def which_prime(num):
    cnt = 0
    for i in range(1 ,num + 1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        return True

n = int(input("How many numbers: "))
nums = []
for i in range(n):
    temp = int(input())
    nums.append(temp)
for i in nums:
    if which_prime(i):
        print(i)
# №2
