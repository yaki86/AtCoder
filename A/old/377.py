import sys
import os
from io import StringIO
import unittest

def resolve():
    S = input()
    if S =="ABC" or S=="ACB" or S=="BAC" or S=="BCA" or S=="CAB" or S=="CBA":
        print("Yes")
    else:
        print("No")
        

    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """BAC"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """AAC"""
        expected = """No"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """ABC"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample4(self):
        input = """ARC"""
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
