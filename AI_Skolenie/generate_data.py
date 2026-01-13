import csv
from faker import Faker
import random

fake = Faker()

with open('user_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Occupation', 'Salary'])
    for i in range(1, 100001):
        first = fake.first_name()
        last = fake.last_name()
        occ = fake.job()
        sal = random.randint(850, 3500)
        writer.writerow([i, first, last, occ, sal])

print("Generated 100,000 rows of user data in user_data.csv")