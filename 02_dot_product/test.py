"""pythonic.py ユニットテスト
"""

import unittest
from pythonic import inprod

class TestInprod(unittest.TestCase):
    """テストケース
    """

    def test_basic(self):
        """基本ケース: 複数要素の通常の内積"""
        vx = [1, 2, 3]
        vy = [3, 2, 1]
        self.assertAlmostEqual(inprod(vx, vy), 10)

    def test_zero_vector(self):
        """ゼロベクトルとの内積"""
        vx = [0, 2, 3]
        vy = [3, 2, 0]
        self.assertAlmostEqual(inprod(vx, vy), 4)

    def test_orthogonal(self):
        """直交するベクトルの内積"""
        vx1 = [1, 0]
        vy1 = [0, 1]
        self.assertAlmostEqual(inprod(vx1, vy1), 0)
        vx2 = [1, 1]
        vy2 = [1, -1]
        self.assertAlmostEqual(inprod(vx2, vy2), 0)

    def test_negative_values(self):
        """負の値を含むベクトルの内積"""
        vx = [-1, 2, 3]
        vy = [3, 2, -1]
        self.assertAlmostEqual(inprod(vx, vy), -2)

    def test_one_dimension(self):
        """1次元ベクトルの内積"""
        vx = [7]
        vy = [3]
        self.assertAlmostEqual(inprod(vx, vy), 21)

    def test_float_values(self):
        """浮動小数点を含むベクトルの内積"""
        vx = [1.0, 3.0, 2.0]
        vy = [2.0, -4.0, 3.0]
        self.assertAlmostEqual(inprod(vx, vy), -4.0)

if __name__ == '__main__':
    unittest.main()


