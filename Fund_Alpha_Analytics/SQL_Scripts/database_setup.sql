USE FundAlphaDB;

-- 1. Rendu puthu managers-a add panrom
INSERT INTO Dim_Manager (Manager_Name, Prior_Experience_Years) VALUES
('Sanjeev Sharma', 15),
('Ankit Patel', 8);

-- 2. Avangala Quant Small Cap (120828) fund kooda link panrom
-- Sanjeev: 2015 la irunthu 2023 dec varaikum (Old Manager)
INSERT INTO Bridge_Fund_Manager (Scheme_Code, Manager_ID, Start_Date, End_Date) 
VALUES (120828, 1, '2015-01-01', '2023-12-31');

-- Ankit: 2024 Jan 1st la irunthu till date varaikum (New Manager - NULL means current)
INSERT INTO Bridge_Fund_Manager (Scheme_Code, Manager_ID, Start_Date, End_Date) 
VALUES (120828, 2, '2024-01-01', NULL);

-- Load aana data-va check panna:
SELECT * FROM Bridge_Fund_Manager;