n = int(input("Enter the number of elements in an array: "))

arr = []

for i in range(1, n + 1):
    num = int(input("Enter the values: "))
    arr.append(num)

arr.sort()

print("The second largest number is: ", arr[n - 2])
