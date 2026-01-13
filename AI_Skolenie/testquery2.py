import psycopg

from dotenv import load_dotenv 
import os 

# pip instsall python-dotenv 

load_dotenv()
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

try:
    # Establish a connection to the database using context manager
    with psycopg.connect(
        host=host,
        dbname=database,
        user=user,
        password=password
    ) as conn:
        # Create a cursor object using context manager
        with conn.cursor() as cur:
            # Execute the query to retrieve all data from the users table
            cur.execute("SELECT * FROM users;")
            
            # Fetch all rows from the query result
            rows = cur.fetchall()
            
            # Print the column names (optional, for better readability)
            if cur.description:
                columns = [desc[0] for desc in cur.description]
                print("Columns:", columns)
            
            # Print each row
            print("Data from users table:")
            for row in rows:
                print(row)
    
except psycopg.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")