import pdb
try:
    x = int(input("Enter the starting integer: "))
    y = int(input("Enter the ending integer (greater than the starting integer): "))
    

    if y <= x:
         temp = y
         y = x
         pdb.set_trace()
         x = temp

    for num in range(x, y + 1):
        if num % 5 == 0 and num % 3 == 0:
                print(f"FizzBuzz {num}")
        elif num % 5 == 0:
                print(f"Fizz {num}")
        elif num % 3 == 0:
                print(f"Buzz {num}")
        else:
            print(num)
except ValueError:
    print("Invalid input. Please enter integers.")