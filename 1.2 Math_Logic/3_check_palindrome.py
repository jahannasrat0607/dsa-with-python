# Check if a number is palindrome or not
# n = 12321

# i = n
# digit = ''
# while n > 0:
#     num = n % 10
#     digit = digit + str(num)
#     n = n // 10
# print(int(digit), i)
# if int(digit) == i:
#     print('Palindrome')
# else:
#     print("Not a palindrome")

# or
n = 123432

num = n
result = 0

while num>0:
    last_digit = num % 10
    result = (result * 10) + last_digit
    num = num // 10
if result == n:
    print("Palindrome")
else:
    print('Not a palindrome')

