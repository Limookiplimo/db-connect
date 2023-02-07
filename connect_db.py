import psycopg2 as db
from faker import Faker

fake = Faker() #faker object
records = [] #empty array to hold data
i=2 #variable to hold new ID(ID one taken by previous test record)

for record in range(1000):
    records.append((i, fake.name(), fake.street_address(), fake.city(), fake.zipcode()))
    i+=1

db_data = tuple(records)

conn_string = "dbname='testdb' host='host.docker.internal' user='user' password='admin123'"
conn = db.connect(conn_string)
cur = conn.cursor()

query = "insert into users(id, name, street, city, zip) values(%s,%s,%s,%s,%s)"

# cur.mogrify(query, db_data)
cur.executemany(query, db_data)
conn.commit()

cur.close()
conn.close()