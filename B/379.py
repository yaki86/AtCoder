import sys
import os
from io import StringIO
import unittest

def resolve():
    N, K = map(int,input().split())
    ha = "O"*K
    S = input()
    flag = 1
    berry = 0

    while(flag>0):
        kenko = S.find(ha)
        if kenko == -1:
            flag = 0
            break
        else:
            berry +=1
            s = list(S)
            for i in range(K):
                s[kenko+i] = "X"
            S = "".join(s)
            
    print(berry)

    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """7 3
OOXOOOO"""
        expected = """1"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """12 2
OXXOOOXOOOOX"""
        expected = """3"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """22 5
XXOOOOOOOOXXOOOOOXXXXX"""
        expected = """2"""
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
