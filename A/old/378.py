import sys
import os
from io import StringIO
import unittest

def resolve():
    A = list(map(int,input().split()))
    count = 0
    count += A.count(1)//2
    count += A.count(2)//2
    count += A.count(3)//2
    count += A.count(4)//2
    
    print(count)

    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """2 1 2 1"""
        expected = """2"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """4 4 4 1"""
        expected = """1"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """1 2 3 4"""
        expected = """0"""
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
