import random

def roll(max_value):
    return random.randint(1, max_value)

def main():

    dice_face = int(input("ENTER DICE FACE: "))
    result = 0
    while result != dice_face:
        result = roll(dice_face)
        print(f"RESULT: {result}")



main()
