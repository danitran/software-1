import random
x = 0
number = random.randint(1, 10)

while True:
    x = float(input("Enter a number between 1 and 10: "))

    if x > number:
        print("Too high")
    elif x < number:
        print("Too low")
    elif x == number:
        print("Correct")
        break
    

