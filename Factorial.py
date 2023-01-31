num = int(input("Enter the number: "))

fact = 1

if num < 0:
    print("Please enter the value in a positive integer")
elif num == 0:
    print("The factorial of value 0 is 1")
else:
    for i in range(1, num+1):
        fact = fact * i
    print(f"The factorial of {num} is {fact}")