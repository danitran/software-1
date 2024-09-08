import random


def num_dice():
    return random.randint(1,6)


def main():
    result = 0
    while result != 6:
        result = num_dice()
        print(f"result: {result}")

main()
