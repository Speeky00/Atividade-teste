
import unittest
from saltotemporal import saltodetempo

class TestSaltodetempo(unittest.TestCase):

    def test_saltodetempo(self):
        self.assertEqual(saltodetempo(1900, 30), 1930)
        self.assertEqual(saltodetempo(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
