# Fund-Manager-Alpha-Analytics
An end-to-end Data Analytics project extracting mutual fund data, modeling a Star Schema in MySQL, calculating Alpha/Beta using Python, and visualizing performance in Power BI.
# 🚀 Quantitative Fund Performance & Alpha Analytics Engine

An end-to-end Data Analytics pipeline built to evaluate Mutual Fund Managers by isolating their true skill (**Alpha**) from the general market trend (**Beta**). 

This project simulates a real-world Quantitative Analyst workflow, integrating API data extraction, database modeling, statistical analysis, and interactive dashboarding.

## 🎯 Business Objective
To determine if a fund manager is truly adding value (outperforming the market) or just riding the market wave, by answering:
1. What is the fund's historical growth?
2. How did the manager perform compared to the Nifty 50 benchmark?
3. Who is the better manager based on risk-adjusted returns (Alpha vs Beta)?

## 🛠️ Technology Stack
*   **Python:** Data Extraction (AMFI APIs, `yfinance`), Data Manipulation (`pandas`), Statistical Modeling (`scipy.stats`).
*   **Database:** MySQL (Star Schema, Fact & Bridge Tables).
*   **Business Intelligence:** Power BI, DAX (Data Analysis Expressions).

## 🏗️ Architecture & Workflow

1.  **Data Engineering (ETL):**
    *   Extracted daily NAV data for specific mutual funds using the AMFI India public API.
    *   Extracted historical Nifty 50 benchmark data using the Yahoo Finance API.
2.  **Data Modeling (MySQL):**
    *   Designed a scalable **Star Schema**.
    *   Implemented a **Bridge Table** (`Bridge_Fund_Manager`) to accurately track manager tenure transitions over time (e.g., Sanjeev from 2015-2023, Ankit from 2024 onwards).
3.  **Quantitative Analysis (Python):**
    *   Joined the Fund NAV and Benchmark datasets.
    *   Applied the **Capital Asset Pricing Model (CAPM)** via Linear Regression to calculate annualized Alpha and Beta.
4.  **Data Visualization (Power BI):**
    *   Connected Power BI directly to the MySQL database.
    *   Utilized **DAX measures** to create dynamic KPI cards.
    *   Built an interactive dashboard allowing stakeholders to filter performance by Manager and visually assess their Alpha/Beta profiles.

## 📊 Dashboard Preview
*(Add your screenshot here by editing this line and dragging/dropping your dashboard_screenshot.png into this space)*

## 💡 Key Insights
*   **Sanjeev Sharma (2015-2023):** Displayed exceptional skill with an **Alpha of +23.87%** while maintaining a lower market risk (**Beta: 0.91**). He is a clear outperformer.
*   **Ankit Patel (2024-Present):** Shows good performance with an **Alpha of +13.71%**, but takes slightly higher market risk (**Beta: 1.03**).

## 📂 Repository Structure
*   `/SQL_Scripts` - Contains the Database Schema and Bridge table setup queries.
*   `/Python_Code` - Contains the ETL scripts for API extraction and the CAPM statistical modeling script.
*   `/Dashboard` - Contains the Power BI (.pbix) file.

## 🚀 How to Run
1.  Run the SQL scripts to setup the `FundAlphaDB`.
2.  Execute `load_data.py` and `load_market.py` to populate the database.
3.  Run `alpha_calc.py` to view the statistical output in the terminal.
4.  Open the `.pbix` file in Power BI Desktop and refresh the data connection.
