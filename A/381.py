import sys
import os
from io import StringIO
import unittest

def resolve():
    N = int(input())
    S = input()
    ans = "Yes"

    if N % 2 == 0:
        ans = "No"
    else:
        
        N1 = S[:int((N+1)/2-1)]
        Ns = S[int((N+1)/2)-1:int((N+1)/2)]       
        N2 = S[int((N+1)/2):]
        
        if Ns != "/":
            ans ="No"
        
        if N1.count("1") != len(N1) :
            ans = "No"
        
        if N2.count("2") != len(N2) :
            ans = "No"

    print(ans)

    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5
11/22"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """1
/"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """4
1/22"""
        expected = """No"""
        self.judge(input, expected)

    def test_sample4(self):
        input = """5
22/11"""
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
