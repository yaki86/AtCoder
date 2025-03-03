import sys
import os
from io import StringIO
import unittest

def resolve():
    S = input()
    T = input()
    flag = 0

    length = min(len(S),len(T))

    for i in range(length):
        if S[i] != T[i]:
            print(i+1)
            flag = 1
            break
    if flag == 0:
        if len(S)==len(T):
            print(0)
        else:
            print(length+1)

    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """abcde
abedc"""
        expected = """3"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """abcde
abcdefg"""
        expected = """6"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """keyence
keyence"""
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
