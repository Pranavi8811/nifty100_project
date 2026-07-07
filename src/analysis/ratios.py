def net_profit_margin(net_profit, sales):
    """
    Calculate Net Profit Margin (NPM)

    Formula:
    (Net Profit / Sales) * 100

    Returns:
        None if sales is 0
    """
    if sales == 0:
        return None

    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    """
    Calculate Operating Profit Margin (OPM)

    Formula:
    (Operating Profit / Sales) * 100

    Returns:
        None if sales is 0
    """
    if sales == 0:
        return None

    return (operating_profit / sales) * 100
def return_on_equity(net_profit, equity, reserves):
    """
    Calculate Return on Equity (ROE)

    Formula:
    (Net Profit / (Equity + Reserves)) * 100

    Returns:
        None if Equity + Reserves <= 0
    """
    capital = equity + reserves

    if capital <= 0:
        return None

    return (net_profit / capital) * 100
def return_on_capital_employed(ebit, equity, reserves, borrowings):
    """
    Calculate Return on Capital Employed (ROCE)

    Formula:
    (EBIT / (Equity + Reserves + Borrowings)) * 100

    Returns:
        None if capital employed <= 0
    """
    capital_employed = equity + reserves + borrowings

    if capital_employed <= 0:
        return None

    return (ebit / capital_employed) * 100
def return_on_assets(net_profit, total_assets):
    """
    Calculate Return on Assets (ROA)

    Formula:
    (Net Profit / Total Assets) * 100

    Returns:
        None if total_assets is 0
    """
    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100
def return_on_assets(net_profit, total_assets):
    """
    Calculate Return on Assets (ROA)

    Formula:
    (Net Profit / Total Assets) * 100

    Returns:
        None if total_assets is 0
    """

    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100
def debt_to_equity(borrowings, equity_capital, reserves):
    """
    Calculate Debt-to-Equity (D/E) Ratio

    Formula:
    Borrowings / (Equity Capital + Reserves)

    Returns:
        0 if borrowings is 0
        None if equity + reserves is 0
    """

    if borrowings == 0:
        return 0

    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return borrowings / equity
print(debt_to_equity(500, 1000, 500))
def debt_to_equity(borrowings, equity_capital, reserves):
    """
    Calculate Debt-to-Equity Ratio

    Formula:
    Borrowings / (Equity Capital + Reserves)

    Returns:
        0 if borrowings == 0
        None if equity + reserves <= 0
    """

    if borrowings == 0:
        return 0

    capital = equity_capital + reserves

    if capital <= 0:
        return None

    return borrowings / capital
print("Debt to Equity :", debt_to_equity(1000, 2000, 1000))
def high_leverage_flag(de_ratio, sector):
    """
    Returns True if D/E > 5 and company is not in Financials sector.
    """

    if de_ratio is None:
        return False

    return de_ratio > 5 and sector.lower() != "financials"
print("High Leverage Flag :", high_leverage_flag(6.2, "Technology"))
print("High Leverage Flag :", high_leverage_flag(6.2, "Financials"))
def interest_coverage_ratio(operating_profit, other_income, interest):
    """
    Calculate Interest Coverage Ratio (ICR)

    Formula:
    (Operating Profit + Other Income) / Interest

    Returns:
        None if interest is 0
    """

    if interest == 0:
        return None

    return (operating_profit + other_income) / interest
print("Interest Coverage Ratio :", interest_coverage_ratio(500, 100, 200))
print("Interest Coverage Ratio :", interest_coverage_ratio(500, 100, 0))
def icr_label(icr):
    """
    Returns a display label for Interest Coverage Ratio.
    """

    if icr is None:
        return "Debt Free"

    return "Covered"
print("ICR Label :", icr_label(3.0))
print("ICR Label :", icr_label(None))
def icr_warning_flag(icr):
    """
    Returns True if ICR is below 1.5.
    """

    if icr is None:
        return False

    return icr < 1.5
print("ICR Warning :", icr_warning_flag(1.2))
print("ICR Warning :", icr_warning_flag(2.5))
print("ICR Warning :", icr_warning_flag(None))
def net_debt(borrowings, cash_and_equivalents):
    """
    Calculate Net Debt

    Formula:
    Borrowings - Cash & Cash Equivalents
    """

    return borrowings - cash_and_equivalents
print("Net Debt :", net_debt(1000, 250))
def asset_turnover(sales, total_assets):
    """
    Calculate Asset Turnover Ratio

    Formula:
    Sales / Total Assets

    Returns:
        None if total_assets is 0
    """

    if total_assets == 0:
        return None

    return sales / total_assets
print("Asset Turnover :", asset_turnover(5000, 2500))
print("Asset Turnover :", asset_turnover(5000, 0))