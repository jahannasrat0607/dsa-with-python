# check if a number is armstrong or not
# 153, 1634 are armstrong numbers

def armstrong_num(num):
    s = num
    n = len(str(num))
    total = 0
    while num>0:
        last_digit = num % 10
        total = total + last_digit ** n
        num = num // 10

    # return total == s
    if total == s:
        return "Armstrong"
    else:
        return "Not Armstrong"

result = armstrong_num(1634)
print(result)

# Time complexity is O(log10(n))
# Space complexity is O(1)
    