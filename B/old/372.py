import sys
import os
from io import StringIO
import unittest
import math

def resolve():
    M = int(input())
    Tmp = M
    A = []
    while(Tmp > 0):
        tmp = math.floor(math.log(Tmp,3))
        if  tmp > 20:
            A.append(20)
            Tmp -= 3**(20)
        else:
            A.append(tmp)
            Tmp -= 3**(tmp)
    
    print(len(A))
    print(" ".join(map(str, A)))

    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """6"""
        expected = """2
1 1"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """100"""
        expected = """4
2 0 2 4"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """59048"""
        expected = """20
0 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9"""
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
