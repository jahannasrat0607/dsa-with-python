# Extract the digits from a given number
n = int(input("Enter the digit :\n"))

while n>0:
    last_digit = n % 10
    print(last_digit, end = " ")
    n = n // 10