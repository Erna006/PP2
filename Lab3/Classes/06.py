# Write a program which can filter prime numbers in a list by using filter function.
# Note: Use lambda to define anonymous functions.
is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
nums = []
n = int(input("How many nums: "))
for i in range(n):
    temp = int(input())
    nums.append(temp)
new = list(filter(is_prime, nums))
print("Prime numbers:", new)
