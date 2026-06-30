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