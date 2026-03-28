nums = [10, 20, 30, 40]
key = int(input("Enter number: "))
for n in nums:
    if n == key:
        print("Found")
        break
else:
    print("Not Found")