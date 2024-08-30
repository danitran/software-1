min_enter = float('inf')
max_enter = float('-inf')

while True:
    enter = input("Enter a number(or click Enter to end): ")
    if enter == '':
        break
    elif enter != '':
        enter = float(enter)
        print(enter)
    else:
        print("Invalid input")
    min_enter = min(min_enter, float(enter))
    max_enter = max(max_enter, float(enter))

print(f"Minimum number entered: {min_enter}")
print(f"Maximum number entered: {max_enter}")

