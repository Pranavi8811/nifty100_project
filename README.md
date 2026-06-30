# Nifty100 Data Foundation

## Overview
This project is part of the Bluestock Fintech Internship Sprint 1. It focuses on building a clean and structured data foundation for Nifty100 company data by performing ETL (Extract, Transform, Load), data validation, and SQLite database integration.

---

## Project Objectives

- Load multiple datasets into SQLite database.
- Clean and normalize raw financial data.
- Validate data quality and integrity.
- Execute SQL queries for analysis.
- Organize project into a professional folder structure.

---

## Project Structure

```
nifty100_project/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── db/
│   ├── nifty100.db
│   └── schema.sql
│
├── notebooks/
│   └── exploratory_queries.sql
│
├── output/
│   ├── load_audit.csv
│   ├── validation_failures.csv
│   └── cleaned CSV files
│
├── src/
│   ├── analysis/
│   │   └── sql_queries.py
│   │
│   └── etl/
│       ├── loader.py
│       ├── validator.py
│       ├── normalizer.py
│       └── load_to_db.py
│
├── requirements.txt
└── tests_setup.py
```

---

## Technologies Used

- Python 3
- Pandas
- SQLite3
- SQL
- Git & GitHub
- Visual Studio Code

---

## Features

- Data Cleaning
- Data Validation
- SQLite Database Creation
- ETL Pipeline
- SQL Data Analysis
- Financial Dataset Processing

---

## Database Tables

- companies
- balancesheet
- cashflow
- financial_ratios
- market_cap
- peer_groups
- profitandloss
- prosandcons
- sectors
- stock_prices

---

## Validation Performed

- Company count verification
- Missing value checks
- Duplicate checks
- Foreign key validation
- Data quality review

---

## How to Run

1. Clone the repository

```
git clone https://github.com/Pranavi8811/nifty100_project.git
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run ETL

```
python src/etl/load_to_db.py
```

4. Execute SQL analysis

```
python src/analysis/sql_queries.py
```

---

## Output

- Cleaned datasets
- SQLite database
- Validation reports
- SQL query results

---

## Author

**K. Pranavi**

Bluestock Fintech Internship 2026

Sprint 1 – Data Foundation
