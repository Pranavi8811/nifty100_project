-- ===========================================
-- Query 1: Total Number of Companies
-- ===========================================
SELECT COUNT(*) AS total_companies
FROM companies;


-- ===========================================
-- Query 2: Top 10 Companies by Market Cap
-- ===========================================
SELECT
    company_id,
    market_cap
FROM market_cap
ORDER BY market_cap DESC
LIMIT 10;


-- ===========================================
-- Query 3: Top 10 Companies by ROE
-- ===========================================
SELECT
    company_id,
    roe
FROM financial_ratios
ORDER BY roe DESC
LIMIT 10;


-- ===========================================
-- Query 4: Top 10 Companies by ROCE
-- ===========================================
SELECT
    company_id,
    roce
FROM financial_ratios
ORDER BY roce DESC
LIMIT 10;


-- ===========================================
-- Query 5: Top 10 Companies by Highest Net Profit
-- ===========================================
SELECT
    company_id,
    MAX(net_profit) AS highest_profit
FROM profit_loss
GROUP BY company_id
ORDER BY highest_profit DESC
LIMIT 10;


-- ===========================================
-- Query 6: Top 10 Companies by Market Cap with ROE
-- ===========================================
SELECT
    m.company_id,
    m.market_cap,
    f.roe
FROM market_cap m
JOIN financial_ratios f
ON m.company_id = f.company_id
ORDER BY m.market_cap DESC
LIMIT 10;


-- ===========================================
-- Query 7: Companies with More Than 10 Years of Balance Sheet Data
-- ===========================================
SELECT
    company_id,
    COUNT(DISTINCT year) AS total_years
FROM balancesheet
GROUP BY company_id
HAVING COUNT(DISTINCT year) > 10
ORDER BY total_years DESC;


-- ===========================================
-- Query 8: Companies with Positive Cash Flow
-- ===========================================
SELECT
    company_id,
    SUM(net_cash_flow) AS total_cash_flow
FROM cashflow
GROUP BY company_id
HAVING total_cash_flow > 0
ORDER BY total_cash_flow DESC;


-- ===========================================
-- Query 9: Top 10 Companies by Sales
-- ===========================================
SELECT
    company_id,
    MAX(sales) AS highest_sales
FROM profit_loss
GROUP BY company_id
ORDER BY highest_sales DESC
LIMIT 10;


-- ===========================================
-- Query 10: Number of Annual Reports Available for Each Company
-- ===========================================
SELECT
    company_id,
    COUNT(annual_report) AS total_reports
FROM documents
GROUP BY company_id
ORDER BY total_reports DESC;-- ===========================================
-- Query 1: Total Number of Companies
-- ===========================================
SELECT COUNT(*) AS total_companies
FROM companies;


-- ===========================================
-- Query 2: Top 10 Companies by Market Cap
-- ===========================================
SELECT
    company_id,
    market_cap
FROM market_cap
ORDER BY market_cap DESC
LIMIT 10;


-- ===========================================
-- Query 3: Top 10 Companies by ROE
-- ===========================================
SELECT
    company_id,
    roe
FROM financial_ratios
ORDER BY roe DESC
LIMIT 10;


-- ===========================================
-- Query 4: Top 10 Companies by ROCE
-- ===========================================
SELECT
    company_id,
    roce
FROM financial_ratios
ORDER BY roce DESC
LIMIT 10;


-- ===========================================
-- Query 5: Top 10 Companies by Highest Net Profit
-- ===========================================
SELECT
    company_id,
    MAX(net_profit) AS highest_profit
FROM profit_loss
GROUP BY company_id
ORDER BY highest_profit DESC
LIMIT 10;


-- ===========================================
-- Query 6: Top 10 Companies by Market Cap with ROE
-- ===========================================
SELECT
    m.company_id,
    m.market_cap,
    f.roe
FROM market_cap m
JOIN financial_ratios f
ON m.company_id = f.company_id
ORDER BY m.market_cap DESC
LIMIT 10;


-- ===========================================
-- Query 7: Companies with More Than 10 Years of Balance Sheet Data
-- ===========================================
SELECT
    company_id,
    COUNT(DISTINCT year) AS total_years
FROM balancesheet
GROUP BY company_id
HAVING COUNT(DISTINCT year) > 10
ORDER BY total_years DESC;


-- ===========================================
-- Query 8: Companies with Positive Cash Flow
-- ===========================================
SELECT
    company_id,
    SUM(net_cash_flow) AS total_cash_flow
FROM cashflow
GROUP BY company_id
HAVING total_cash_flow > 0
ORDER BY total_cash_flow DESC;


-- ===========================================
-- Query 9: Top 10 Companies by Sales
-- ===========================================
SELECT
    company_id,
    MAX(sales) AS highest_sales
FROM profit_loss
GROUP BY company_id
ORDER BY highest_sales DESC
LIMIT 10;


-- ===========================================
-- Query 10: Number of Annual Reports Available for Each Company
-- ===========================================
SELECT
    company_id,
    COUNT(annual_report) AS total_reports
FROM documents
GROUP BY company_id
ORDER BY total_reports DESC;


