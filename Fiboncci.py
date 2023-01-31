num = int(input("Enter the value "))

n1, n2 = 0, 1
count = 0

if num <= 0:
    print("Please enter a positive integer")

elif num == 1:
    print("Fibonacci sequence upto 1 is 1")

else:
    print(f"The Fibonacci sequence of {num} is:")
    while count < num:
        print(n1)
        n = n1 + n2

        n1 = n2
        n2 = n
        count += 1
