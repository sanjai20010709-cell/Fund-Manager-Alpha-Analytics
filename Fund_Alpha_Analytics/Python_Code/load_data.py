import requests
import mysql.connector
from datetime import datetime

# 1. Database Connection Setup
# Unga local MySQL username & password-a inga mathikonga
db = mysql.connector.connect(
    host="localhost",
    user="root",          
    password="sparx0709",  # <-- INGA UNGA PASSWORD PODUNGA
    database="FundAlphaDB"
)
cursor = db.cursor()

# Target Funds: Quant Small Cap, Motilal Oswal Midcap, ICICI Pru Large Cap
scheme_codes = [120828, 128155, 120586]

for code in scheme_codes:
    print(f"Fetching data for Scheme Code: {code}...")
    
    # 2. Extract Data from AMFI API
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()
    
    # 3. Load into Dim_Fund Table
    fund_name = data['meta']['scheme_name']
    amc_name = data['meta']['fund_house']
    category = data['meta']['scheme_category']
    
    # INSERT IGNORE use panrathala, already data iruntha duplicate aagathu
    insert_fund_query = """
    INSERT IGNORE INTO Dim_Fund (Scheme_Code, Fund_Name, Category, AMC_Name)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_fund_query, (code, fund_name, category, amc_name))
    
    # 4. Transform & Load Daily NAVs into Fact_Daily_NAV Table
    nav_data = data['data']
    print(f"Found {len(nav_data)} days of NAV data. Database-la load aaguthu, wait pannunga...")
    
    insert_nav_query = """
    INSERT INTO Fact_Daily_NAV (Scheme_Code, Nav_Date, NAV_Value) 
    VALUES (%s, %s, %s)
    """
    
    # Batch insert-kaga empty list create panrom
    records_to_insert = []
    
    for record in nav_data:
        # Date format 'DD-MM-YYYY' la irunthu MySQL format 'YYYY-MM-DD' ku mathurom
        nav_date = datetime.strptime(record['date'], '%d-%m-%Y').strftime('%Y-%m-%d')
        nav_value = float(record['nav'])
        records_to_insert.append((code, nav_date, nav_value))
    
    # executemany use panni thousands of rows-a single shot-la insert panrom (for speed)
    cursor.executemany(insert_nav_query, records_to_insert)
    db.commit()
    
    print(f"Success! {fund_name} data MySQL-la load aaiduchu.\n")

print("Ellam mudinjithu! Unga MySQL Workbench-la check pannunga.")
cursor.close()
db.close()