fizz_buzz =[]
try: 
    start = int(input("What number do you want to start with? "))
    end = int(input("What number do you want to end with? "))
except (ValueError):
    print("Please enter a number")
else:
    end +=1
    for x in range(start,end):
        if (x % 3) == 0:
            if (x % 5) == 0:
                fizz_buzz.append("Fizz buzz")
                continue
            fizz_buzz.append("Fizz")
        elif (x % 5) == 0:
            fizz_buzz.append("Buzz")
        else:
            fizz_buzz.append(x)
    print(fizz_buzz)