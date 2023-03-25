import sys
import json
import sqlite3

# Define SQLite schema
schema = """
CREATE TABLE quotes (
    id INTEGER PRIMARY KEY,
    text TEXT,
    author TEXT,
    tags TEXT
);
"""

fhin = sys.argv[1]
fhout = fhin+'.sqlite'

print(f"converting {fhin} to {fhout}...")

# Open connection to SQLite database
conn = sqlite3.connect(fhout)

# Create cursor object to execute SQLite commands
c = conn.cursor()

# Create quotes table
c.execute(schema)

# Load JSON data from file
with open(fhin, 'r') as f:
    data = json.load(f)

# Insert data into quotes table
for quote in data:
    c.execute("INSERT INTO quotes (text, author, tags) VALUES (?, ?, ?)",
              (quote['text'], quote['author'], ','.join(quote['tags'])))

# Commit changes and close connection
conn.commit()
conn.close()

print('done.')
