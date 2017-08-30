import unittest
from interpreter import Interpreter

class TestInterpreter(unittest.TestCase):

    def test_negative_discr(self):
        s = Interpreter()
        self.assertRaises(Exception,s.compute,'ex-3.txt')

    def test_positive(self):
        s = Interpreter()
        self.assertEquals(s.compute('ex-2.py'),[-10.5,8])

if __name__ == '__main__':
    unittest.main()