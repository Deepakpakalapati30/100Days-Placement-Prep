nums=[1,2,2,3,2,4]
key=int(input("enter number:"))
count=0
for n in nums:
    if n==key:
        count+=1
        print("Count:",count)
