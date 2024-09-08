def gallons_to_litres(gallons):
    return gallons * 3.78541

def main_gallons_to_litres():
    while True:
        gallons = float(input("Enter the quantity of gasoline in gallons (negative to quit): "))
        if gallons < 0:
            print("Exiting the program.")
            break
        litres = gallons_to_litres(gallons)
        print(f"{gallons} gallons is {litres:.2f} litres.")

main_gallons_to_litres()
