a = int(input("Enter a:"))

if((a % 3 == 0) & (a % 5 == 0)):
    print("a is divisible by both 3 and 5")
elif (a % 3 == 0) or (a % 5 == 0):
    print("a is divisible by either 3 or 5, but not both")
else:
    print("a is not divisible by both 3 and 5")