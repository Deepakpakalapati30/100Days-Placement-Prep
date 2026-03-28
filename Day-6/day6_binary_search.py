nums = [1, 2, 3, 4, 5, 6]
key = int(input("Enter number: "))
low = 0
high = len(nums) - 1
found = False
while low <= high:
    mid = (low + high) // 2

    if nums[mid] == key:
        found = True
        break
    elif nums[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
if found:
    print("Found")
else:
    print("Not Found")