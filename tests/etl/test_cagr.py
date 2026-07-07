import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/analysis")
    )
)

from cagr import *


class TestCAGR(unittest.TestCase):

    def test_revenue_cagr(self):
        self.assertAlmostEqual(
            revenue_cagr(100, 200, 5),
            14.869835499703509
        )

    def test_pat_cagr(self):
        self.assertAlmostEqual(
            pat_cagr(100, 200, 5),
            14.869835499703509
        )

    def test_eps_cagr(self):
        self.assertAlmostEqual(
            eps_cagr(100, 200, 5),
            14.869835499703509
        )

    def test_zero_base(self):
        self.assertEqual(
            cagr_flag(0, 200, 5),
            "ZERO_BASE"
        )

    def test_turnaround(self):
        self.assertEqual(
            cagr_flag(-100, 200, 5),
            "TURNAROUND"
        )


if __name__ == "__main__":
    unittest.main()