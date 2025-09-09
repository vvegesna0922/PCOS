# database.py
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("pcos_tracker.db", check_same_thread=False)
cursor = conn.cursor()

# Create a table for PCOS health data
cursor.execute("""
CREATE TABLE IF NOT EXISTS health_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    period_length INTEGER,
    symptoms TEXT,
    mood TEXT
)
""")

conn.commit()
