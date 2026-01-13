
import psycopg

def get_it_users():
    """
    Connects to the PostgreSQL database and retrieves all users with the occupation 'computer department'.

    Returns:
        A list of tuples, where each tuple represents a user.
    """
    conn = None
    try:
        # Connect to the database
        conn = psycopg.connect(
            dbname="testdb",
            user="postgres",
            password="", 
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Execute the query
        cur.execute("SELECT * FROM users WHERE occupation = 'computer department'")

        # Fetch all the results
        users = cur.fetchall()

        # Close the cursor
        cur.close()

        return users

    except (Exception, psycopg.DatabaseError) as error:
        print(f"Error connecting to the database or fetching data: {error}")
        return []

    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    it_users = get_it_users()
    if it_users:
        print("Users in the IT department:")
        for user in it_users:
            print(user)
    else:
        print("No users found in the IT department or an error occurred.")
