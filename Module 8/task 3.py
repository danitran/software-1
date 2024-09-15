import geopy.distance

def calculate_distance(icao_code1, icao_code2):
  """
  Calculates the distance between two airports using their coordinates.
  """
  conn = psycopg2.connect(  # Replace with your database connection details
      database="your_database",
      user="your_username",
      password="your_password",
      host="your_host",
      port="your_port"
  )
  cursor = conn.cursor()
  cursor.execute("SELECT latitude, longitude FROM airport WHERE ident IN (%s, %s)", (icao_code1.upper(), icao_code2.upper()))
  rows = cursor.fetchall()
  conn.close()

  if len(rows) != 2:
      print("One or both airports not found in the database.")
      return

  coordinates1 = (rows[0][0], rows[0][1])
  coordinates2 = (rows[1][0], rows[1][1])
  distance_in_km = geopy.distance.geodesic(coordinates1, coordinates2).km
  print(f"The distance between the two airports is approximately {distance_in_km:.2f} kilometers.")

icao_code1 = input("Enter the ICAO code of the first airport: ")
icao_code2 = input("Enter the ICAO code of the second airport: ")
calculate_distance(icao_code1.upper(), icao_code2.upper())