num = int(input("Enter the number: "))

temp = num
reverse = 0
while temp > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10

if temp == reverse:
    print('Palindrome')
else:
    print("Not Palindrome")