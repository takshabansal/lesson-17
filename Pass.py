a=int(input("Enter a number:"))
for x in range(a):
    if x % 20 == 0:
        print("Twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("Fizz")
    elif x % 3 == 0:
        print("Buzz")
    else:
        print(x)