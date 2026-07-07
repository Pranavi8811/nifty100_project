def cagr(start, end, years):
    """
    Calculate Compound Annual Growth Rate (CAGR).
    """

    if years <= 0:
        return None

    if start <= 0:
        return None

    if end <= 0:
        return None

    return ((end / start) ** (1 / years) - 1) * 100


def revenue_cagr(start_revenue, end_revenue, years):
    """
    Calculate Revenue CAGR.
    """
    return cagr(start_revenue, end_revenue, years)


def pat_cagr(start_pat, end_pat, years):
    """
    Calculate Profit After Tax (PAT) CAGR.
    """
    return cagr(start_pat, end_pat, years)


def eps_cagr(start_eps, end_eps, years):
    """
    Calculate EPS CAGR.
    """
    return cagr(start_eps, end_eps, years)
def cagr_flag(start, end, years):
    """
    Returns a flag based on CAGR edge cases.
    """

    if years <= 0:
        return "INSUFFICIENT_DATA"

    if start == 0:
        return "ZERO_BASE"

    if start > 0 and end > 0:
        return "NORMAL"

    if start > 0 and end < 0:
        return "DECLINE_TO_LOSS"

    if start < 0 and end > 0:
        return "TURNAROUND"

    if start < 0 and end < 0:
        return "BOTH_NEGATIVE"

    return None


print("Revenue CAGR:", revenue_cagr(100, 200, 5))
print("PAT CAGR:", pat_cagr(50, 100, 5))
print("EPS CAGR:", eps_cagr(10, 20, 5))
print("\n--- Edge Cases ---")

print("Years = 0:", cagr(100, 200, 0))
print("Negative Start:", cagr(-100, 200, 5))
print("Negative End:", cagr(100, -200, 5))
print("Zero Start:", cagr(0, 200, 5))
print("Zero End:", cagr(100, 0, 5))
print("\n--- CAGR Flags ---")

print(cagr_flag(100, 200, 5))
print(cagr_flag(100, -200, 5))
print(cagr_flag(-100, 200, 5))
print(cagr_flag(-100, -200, 5))
print(cagr_flag(0, 200, 5))
print(cagr_flag(100, 200, 0))