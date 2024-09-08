import random

num_dice = int(input("Give me the number of dices: "))

total_sum = 0

for _ in range(num_dice):
    roll = random.randint(1, 6)
    total_sum += roll

print(f"All of dice {num_dice} times you roll: {total_sum}")
