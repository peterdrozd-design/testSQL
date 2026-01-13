import yaml
import psycopg


# pip install pyyaml

# Load YAML configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

db = config["database"]

host = db["host"]
database = db["name"]
user = db["user"]
password = db["password"]



try:
    with psycopg.connect(
        host=host,
        dbname=database,
        user=user,
        password=password
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users;")
            rows = cur.fetchall()

            if cur.description:
                columns = [desc[0] for desc in cur.description]
                print("Columns:", columns)

            print("Data from users table:")
            for row in rows:
                print(row)

except psycopg.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")