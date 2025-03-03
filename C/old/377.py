import sys
import os
from io import StringIO
import unittest

def resolve():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for l in range(M)]
    st =  ["o"] * N
    start = [list(st) for _ in range(N)]
    count = 0

    for i in range(M):
        start[ab[i][0]-1][ab[i][1]-1]="x"

        if ab[i][0]-1 > 0 and ab[i][1]-2 >0:
            start[ab[i][0]-1-1][ab[i][1]-2-1]="x"

        if ab[i][0]-2 > 0 and ab[i][1]-1 >0:
            start[ab[i][0]-2-1][ab[i][1]-1-1]="x"

        if ab[i][0]-2 > 0 and ab[i][1]+1 < N:
            start[ab[i][0]-2-1][ab[i][1]+1-1]="x"

        if ab[i][0]-1 > 0 and ab[i][1]+2 < N:
            start[ab[i][0]-1-1][ab[i][1]+2-1]="x"

        if ab[i][0]+1 < N and ab[i][1]+2 < N:
            start[ab[i][0]+1-1][ab[i][1]+2-1]="x"

        if ab[i][0]+2 < N and ab[i][1]+1 < N:
            start[ab[i][0]+2-1][ab[i][1]+1-1]="x"

        if ab[i][0]+2 < N  and ab[i][1]-1 >0:
            start[ab[i][0]+2-1][ab[i][1]-1-1]="x"

        if ab[i][0]+1 < N and ab[i][1]-2 >0:
            start[ab[i][0]+1-1][ab[i][1]-2-1]="x"
            
    for j in range(N):
        count += start[j].count("o")

    print(count)
        
    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """8 6
1 4
2 1
3 8
4 5
5 2
8 3"""
        expected = """38"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """1000000000 1
1 1"""
        expected = """999999999999999997"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """20 10
1 4
7 11
7 15
8 10
11 6
12 5
13 1
15 2
20 10
20 15"""
        expected = """338"""
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
