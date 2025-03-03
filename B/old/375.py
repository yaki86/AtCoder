import sys
import os
from io import StringIO
import unittest

def resolve():
    N = int(input())
    XY = [list(map(int, input().split())) for l in range(N)]
    cost = 0
    
    cost += ((XY[0][0])**2 + (XY[0][1])**(2))**(0.5)
    for i in range(N-1):        
        cost += ((XY[i][0]-XY[i+1][0])**2 + (XY[i][1]-XY[i+1][1])**2)**(0.5)
    cost += ((XY[N-1][0])**2 + (XY[N-1][1])**(2))**(0.5)

    print(cost)
    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """2
1 2
-1 0"""
        expected = """6.06449510224597979401"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """7
-14142 13562
-17320 50807
-22360 67977
24494 89742
-26457 51311
28284 27124
31622 77660"""
        expected = """384694.57587932075868509383"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """5
-100000 100000
100000 -100000
-100000 100000
100000 -100000
-100000 100000"""
        expected = """1414213.56237309504880168872"""
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
