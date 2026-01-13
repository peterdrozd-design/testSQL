import sqlite3
import csv

conn = sqlite3.connect('test_db.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
conn.close()

with open('user_data4.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'first_name', 'last_name', 'email', 'occupation', 'salary', 'created_at'])
    writer.writerows(rows)

print("Data exported to user_data4.csv")