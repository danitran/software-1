import math

def pizza_price_per_square_meter(diameter, price):
    radius  = diameter / 2
    area    = math.pi * radius ** 2 / 10000
    return price / area

def main_pizza_comparison():
    diameter1   = float(input("Enter the diameter of the first pizza in cm: "))
    price1      = float(input("Enter the price of the first pizza in euros: "))
    diameter2   = float(input("Enter the diameter of the second pizza in cm: "))
    price2      = float(input("Enter the price of the second pizza in euros: "))

    unit_price1 = pizza_price_per_square_meter(diameter1, price1)
    unit_price2 = pizza_price_per_square_meter(diameter2, price2)

    print(f"The first pizza costs {unit_price1:.2f} euros per square meter.")
    print(f"The second pizza costs {unit_price2:.2f} euros per square meter.")

    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price1 > unit_price2:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")

main_pizza_comparison()
