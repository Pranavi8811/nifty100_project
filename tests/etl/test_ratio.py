import unittest
import sys
import os

# Add src/analysis to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/analysis")
    )
)

from ratios import *

class TestRatios(unittest.TestCase):

    def test_net_profit_margin(self):
        self.assertEqual(
            net_profit_margin(500, 1000),
            50.0
        )

    def test_debt_to_equity(self):
        self.assertAlmostEqual(
            debt_to_equity(1000, 2000, 1000),
            0.3333333333333333
        )

    def test_return_on_assets(self):
        self.assertEqual(
            return_on_assets(500, 5000),
            10.0
        )

    def test_interest_coverage_ratio(self):
        self.assertEqual(
            interest_coverage_ratio(1000, 500, 300),
            5.0
        )

    def test_asset_turnover(self):
        self.assertEqual(
            asset_turnover(10000, 5000),
            2.0
        )

    def test_net_debt(self):
        self.assertEqual(
            net_debt(1000, 250),
            750
        )
    def test_icr_label(self):
       self.assertEqual(
        icr_label(None),
        "Debt Free"
    )
    def test_icr_warning(self):
     self.assertTrue(icr_warning_flag(1.2))
     self.assertFalse(icr_warning_flag(2.0))
if __name__ == "__main__":
    unittest.main()