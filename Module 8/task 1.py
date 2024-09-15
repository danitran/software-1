import psycopg2  # Assuming you have PostgreSQL connection details

def get_airport_info(icao_code):
  """
  Fetches airport name and location (town) from the database.
  """
  conn = psycopg2.connect(  # Replace with your database connection details
      database="your_database",
      user="your_username",
      password="your_password",
      host="your_host",
      port="your_port"
  )
  cursor = conn.cursor()
  cursor.execute("SELECT name, location FROM airport WHERE ident = %s", (icao_code,))
  row = cursor.fetchone()
  conn.close()
  if row:
      name, location = row
      print("Airport Name:", name)
      print("Location:", location)
  else:
      print("Airport not found in the database.")

icao_code = input("Enter the ICAO code: ")
get_airport_info(icao_code.upper())  # Convert ICAO code to uppercase