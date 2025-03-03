import sys
import os
from io import StringIO
import unittest

def resolve():
    N = list(input())
    print(N[1]+N[2]+N[0]+" "+ N[2]+N[0]+N[1])


    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """379"""
        expected = """793 937"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """919"""
        expected = """199 991"""
        self.judge(input, expected)

    def judge(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    if "ATCODER" in os.environ:
        resolve()
    else:
        unittest.main(verbosity=2)
