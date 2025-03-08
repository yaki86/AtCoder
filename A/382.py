import sys
import os
from io import StringIO
import unittest

def resolve():
    N, D = map(int, input().split())
    S = input()

    cookie = S.count("@")
    
    print(N - cookie + D)

    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5 2
.@@.@"""
        expected = """4"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3 3
@@@"""
        expected = """3"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """10 4
@@@.@@.@@."""
        expected = """7"""
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
