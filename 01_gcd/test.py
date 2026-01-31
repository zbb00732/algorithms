"""pythonic.py ユニットテスト
"""

import unittest
from pythonic import gcd

class TestGcd(unittest.TestCase):
    """テストケース
    """

    def test_gcd(self):
        """最大公約数を返すこと
        """
        self.assertEqual(gcd(480, 72), 24)

    def test_gcd_reversed(self):
        """m < n のとき入れ替えが発生しても正しい結果を返すこと
        """
        self.assertEqual(gcd(72, 480), 24)

    def test_gcd_coprime(self):
        """互いに素な場合は1を返すこと
        """
        self.assertEqual(gcd(13, 7), 1)

    def test_gcd_equal(self):
        """同じ値の場合はその値を返すこと
        """
        self.assertEqual(gcd(12, 12), 12)

    def test_gcd_with_zero(self):
        """一方が0の場合はもう一方を返すこと
        """
        self.assertEqual(gcd(7, 0), 7)
        self.assertEqual(gcd(0, 7), 7)

if __name__ == '__main__':
    unittest.main()

