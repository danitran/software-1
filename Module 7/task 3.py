airports = {}

while True:
    choice = input("Enter 'new', 'fetch', or 'quit': ")

    if choice == 'new':
        icao_code = input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")
        airports[icao_code] = name
        print("Airport added successfully.")
    elif choice == 'fetch':
        icao_code = input("Enter the ICAO code: ")
        if icao_code in airports:
            print("Airport name:", airports[icao_code])
        else:
            print("Airport not found.")
    elif choice == 'quit':
        break
    else:
        print("Invalid choice. Please try again.")