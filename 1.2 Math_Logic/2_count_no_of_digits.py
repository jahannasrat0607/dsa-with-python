# Count the total number of digits in a given number

# method 1
n = input("Enter your input:\n")
counter = 0
for _ in range(len(n)):
    counter += 1
print("Number of digits are:", counter)

# time complexity is O(d), where d is number of digits and space complexity is O(1)

# method 2
num = 5387
count = 0
while num != 0:
    count += 1
    num = num//10
print("Number of digits are:", count)

# time complexity is O(log10(n)) and space complexity is O(1)

# method 3

# log10(5438) = 3.735
# log10(177715) = 5.249
# log10(973) = 2.988

from math import log10
num = 5387768
def count_digits(num):
    return int(log10(num) + 1)
print("Number of digits are:", count_digits(num))

# Time complexity O(1) and space complexity is also O(1)
