import sys
import os
from io import StringIO
import unittest

def resolve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    A = list(map(int, input().split()))


    walk = 0
    dead = False

    if X[0] != 1:
        dead = True
    else:
        HP = A[0]
        for i in range(M - 1):
            if dead:
                break
            tmpWalk = X[i + 1] - X[i] - 1
            walk += tmpWalk * (tmpWalk + 1) / 2
            HP -= tmpWalk
            if HP < 0:
                dead = True
            elif HP >= 1 :
                walk += HP*(X[i + 1] - X[i])
                HP += A[i+1]
            else:
                HP += A[i + 1]
        
        if not dead:
            tmpWalk = N - X[M - 1]
            walk += tmpWalk * (tmpWalk + 1) / 2
            HP -= tmpWalk
            if HP != 1:
                dead = True

    if dead:
        print(-1)
    else:
        print(int(walk))

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """6 2
1 5
4 1"""
        expected = """11"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """10 3
1 4 8
4 2 4"""
        expected = """-1"""
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
