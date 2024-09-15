seasons = ("winter", "spring", "summer", "autumn")

month_number = int(input("Enter the month number (1-12): "))

if month_number in range(1, 4):
    season = seasons[0]
elif month_number in range(4, 7):
    season = seasons[1]
elif month_number in range(7, 10):
    season = seasons[2]
else:
    season = seasons[3]

print("The season for month", month_number, "is", season)