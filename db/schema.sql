CREATE TABLE IF NOT EXISTS companies (
    id TEXT PRIMARY KEY,
    company_name TEXT,
    website TEXT,
    roe_percentage REAL
);

CREATE TABLE IF NOT EXISTS sectors (
    sector_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sector_name TEXT
);

CREATE TABLE IF NOT EXISTS market_cap (
    company_id TEXT,
    market_cap REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE IF NOT EXISTS financial_ratios (
    company_id TEXT,
    roe REAL,
    roce REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE IF NOT EXISTS stock_prices (
    company_id TEXT,
    price_date TEXT,
    close_price REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);
CREATE TABLE IF NOT EXISTS profit_loss (
    company_id TEXT,
    year INTEGER,
    sales REAL,
    net_profit REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);
CREATE TABLE IF NOT EXISTS balancesheet (
    company_id TEXT,
    year INTEGER,
    equity_capital REAL,
    reserves REAL,
    borrowings REAL,
    other_liabilities REAL,
    total_liabilities REAL,
    fixed_assets REAL,
    other_asset REAL,
    total_assets REAL
);
CREATE TABLE IF NOT EXISTS cashflow (
    company_id TEXT,
    year INTEGER,
    operating_activity REAL,
    investing_activity REAL,
    financing_activity REAL,
    net_cash_flow REAL
);
CREATE TABLE IF NOT EXISTS analysis (
    company_id TEXT,
    compounded_sales_growth REAL,
    compounded_profit_growth REAL,
    stock_price_cagr REAL,
    roe REAL
);
CREATE TABLE IF NOT EXISTS peer_groups (
    id INTEGER,
    sector_name TEXT,
    company_id TEXT,
    is_leader BOOLEAN
);
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER,
    company_id TEXT,
    year INTEGER,
    annual_report TEXT
);
CREATE TABLE IF NOT EXISTS prosandcons (
    id INTEGER,
    company_id TEXT,
    pros TEXT,
    cons TEXT
);