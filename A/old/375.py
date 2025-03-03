import sys
import os
from io import StringIO
import unittest

def resolve():
    N = int(input())
    S = input()
    count = 0

    for i in range(N-2):
        if S[i] == "#" and S[i+1] == "." and S[i+2] =="#":
            count += 1
    print(count)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """6
#.##.#"""
        expected = """2"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """1
#"""
        expected = """0"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """9
##.#.#.##"""
        expected = """3"""
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
