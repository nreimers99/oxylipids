import csv
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('ox_pdt.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS ox_pdt_1 (
                    ID TEXT,
                    parent TEXT,
                    mz REAL,
                    rt REAL,
                    ccs REAL,
                    adduct TEXT,
                    modification TEXT
                    )''')

# Read data from the CSV file and insert into the table
with open('PLPC_TEST.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if it exists
    for row in reader:
        sql_insert = f"INSERT INTO ox_pdt_1 (ID, parent, mz, rt, ccs, adduct, modification) VALUES ({row[0]})"

# Commit changes and close the connection
conn.commit()
conn.close()