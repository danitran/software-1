names = set()

while True:
    name = input("Enter a name (or press Enter to quit): ")
    if not name:
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("Input names:")
for name in names:
    print(name)