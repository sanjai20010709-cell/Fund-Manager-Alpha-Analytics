import yfinance as yf
import mysql.connector
from datetime import datetime

# 1. Database Connection Setup
db = mysql.connector.connect(
    host="localhost",
    user="root",          
    password="sparx0709",  # <-- INGA UNGA PASSWORD PODUNGA
    database="FundAlphaDB"
)
cursor = db.cursor()

print("Fetching Nifty 50 Data from Yahoo Finance...")

# 2. Extract Data from Yahoo Finance (^NSEI is the symbol for Nifty 50)
nifty = yf.Ticker("^NSEI")
# Last 10 years data edukkurom (namma fund data kooda match panna)
hist = nifty.history(period="10y")

print(f"Found {len(hist)} days of Nifty 50 data. Database-la load aaguthu, wait pannunga...")

# 3. Load into Fact_Benchmark Table
insert_query = """
INSERT INTO Fact_Benchmark (Index_Name, Index_Date, Close_Value) 
VALUES (%s, %s, %s)
"""

# Batch insert-kaga empty list create panrom
records_to_insert = []

for index, row in hist.iterrows():
    # Date and closing value edukkurom
    index_date = index.strftime('%Y-%m-%d')
    close_value = float(row['Close'])
    records_to_insert.append(('Nifty 50', index_date, close_value))

# executemany use panni single shot-la insert panrom
cursor.executemany(insert_query, records_to_insert)
db.commit()

print("Success! Nifty 50 Benchmark data MySQL-la load aaiduchu.")

cursor.close()
db.close()