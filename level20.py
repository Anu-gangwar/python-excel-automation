import sqlite3

conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    product TEXT,
    sales INTEGER,
    region TEXT
)
''')

# Clear old data to prevent duplicates
cursor.execute('DELETE FROM orders')

# Insert fresh data
orders_data = [
    ('Laptop', 1200, 'North'),
    ('Mouse', 25, 'South'),
    ('Keyboard', 75, 'East'),
    ('Monitor', 300, 'West')
]
cursor.executemany('INSERT INTO orders (product, sales, region) VALUES (?,?,?)', orders_data)

# Query data
cursor.execute('SELECT product, sales FROM orders WHERE sales > 100')
rows = cursor.fetchall()

print("High value orders:")
for row in rows:
    print(f"{row[0]}: ${row[1]}")

# Commit and close AT THE VERY END
conn.commit()
conn.close()
print("\n✅ Database created: sales.db")