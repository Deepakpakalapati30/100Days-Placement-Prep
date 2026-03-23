a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))

if a >= b and a >= c and a >= d:
    print("A is largest")
elif b >= a and b >= c and b >= d:
    print("B is largest")
elif c >= a and c >= b and c >= d:
    print("C is largest")
else:
    print("D is largest")