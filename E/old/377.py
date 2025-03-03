import sys
import os
from io import StringIO
import unittest

def resolve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    for i in range(K):
        tmp = P
        


    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """6 3
5 6 3 1 2 4"""
        expected = """6 1 3 2 4 5"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """5 1000000000000000000
1 2 3 4 5"""
        expected = """1 2 3 4 5"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """29 51912426
7 24 8 23 6 1 4 19 11 18 20 9 17 28 22 27 15 2 12 26 10 13 14 25 5 29 3 21 16"""
        expected = """18 23 16 24 21 10 2 27 19 7 12 8 13 5 15 26 17 4 3 9 1 22 25 14 28 11 29 6 20"""
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
