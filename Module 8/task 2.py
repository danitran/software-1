import psycopg2  # Assuming you have PostgreSQL connection details

def list_airports_by_area_code(area_code):
  """
  Lists airports located in the specified country ordered by airport type.
  """
  conn = psycopg2.connect(  # Replace with your database connection details
      database="your_database",
      user="your_username",
      password="your_password",
      host="your_host",
      port="your_port"
  )
  cursor = conn.cursor()
  cursor.execute("SELECT type, COUNT(*) FROM airport WHERE type LIKE %s GROUP BY type ORDER BY type", (area_code + '%',))
  for row in cursor:
      airport_type, count = row
      print(f"{count} {airport_type.lower()} airports")
  conn.close()

area_code = input("Enter the area code (e.g., FI): ")
list_airports_by_area_code(area_code.upper())