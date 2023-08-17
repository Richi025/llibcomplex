import Libcplx as lc
import unittest

class TestStringMethods(unittest.TestCase):

    def test_cplxsum(self):
        suma = lc.cplxsum((3, 5),(-2.6, 6.8))
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)

if __name__ == '__main__':
    unittest.main()

