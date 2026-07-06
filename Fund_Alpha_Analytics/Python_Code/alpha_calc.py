import pandas as pd
import mysql.connector
from scipy import stats

# 1. Database Connection Setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sparx0709",  # <-- INGA UNGA PASSWORD PODUNGA
    database="FundAlphaDB"
)

# 2. SQL Query to get Aligned Data (Fund NAV vs Nifty 50)
query = """
SELECT 
    n.Nav_Date, 
    n.NAV_Value, 
    b.Close_Value as Nifty_Value
FROM Fact_Daily_NAV n
JOIN Fact_Benchmark b ON n.Nav_Date = b.Index_Date
WHERE n.Scheme_Code = 120828
ORDER BY n.Nav_Date
"""

cursor = db.cursor()
cursor.execute(query)
records = cursor.fetchall()
cols = [desc[0] for desc in cursor.description]

# 3. Create DataFrame and Calculate Daily Profit/Loss %
df = pd.DataFrame(records, columns=cols)
df['Nav_Date'] = pd.to_datetime(df['Nav_Date'])

# ---> INGA THAAN FIX IRUKKU: Object-a Float a mathurom <---
df['NAV_Value'] = df['NAV_Value'].astype(float)
df['Nifty_Value'] = df['Nifty_Value'].astype(float)
# ---------------------------------------------------------

# pct_change() use panni daily percentage return calculate panrom
df['Fund_Return'] = df['NAV_Value'].pct_change() * 100
df['Market_Return'] = df['Nifty_Value'].pct_change() * 100
df = df.dropna()

# 4. Split Data by Manager Tenure
# Sanjeev (Old Manager): 2023 full year
sanjeev_data = df[(df['Nav_Date'] >= '2023-01-01') & (df['Nav_Date'] <= '2023-12-31')]

# Ankit (New Manager): 2024 full year
ankit_data = df[(df['Nav_Date'] >= '2024-01-01') & (df['Nav_Date'] <= '2024-12-31')]

# 5. Function to Calculate Alpha and Beta
def calculate_metrics(data, manager_name):
    # Scipy stats use panni Linear Regression panrom (CAPM Model)
    beta, daily_alpha, r_value, p_value, std_err = stats.linregress(data['Market_Return'], data['Fund_Return'])
    
    # Daily alpha-va Annual Alpha (1 year = approx 252 trading days) a mathurom
    annual_alpha = daily_alpha * 252
    
    print(f"--- {manager_name} Performance ---")
    print(f"Beta (Market Risk)  : {beta:.2f}")
    print(f"Alpha (Manager Skill): {annual_alpha:.2f}% (Annualized)\n")

print("\n🚀 Calculating Fund Manager Alpha for Quant Small Cap...\n")
calculate_metrics(sanjeev_data, "Sanjeev (2023)")
calculate_metrics(ankit_data, "Ankit (2024)")

db.close()