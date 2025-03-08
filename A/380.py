import sys
import os
from io import StringIO
import unittest

def resolve():
    N = input()
    ans = "Yes"
    if N.count("1") != 1:
        ans = "No"
    elif N.count("2") != 2:
        ans = "No"
    elif N.count("3") != 3:
        ans = "No"
    
    print(ans)

    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """123233"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """123234"""
        expected = """No"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """323132"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample4(self):
        input = """500000"""
        expected = """No"""
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
