import sys
import os
from io import StringIO
import unittest

def resolve():
    N, M = map(int,input().split())
    akago = []
    for i in range(M):
        a,b = input().split()
        akago.append([int(a),b])

    A = [0]*N

    for i in range(M):
        if akago[i][1] == "M" and A[akago[i][0]-1] == 0:
            A[akago[i][0]-1] = 1
            print("Yes")
        else:
            print("No")


    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """2 4
1 M
1 M
2 F
2 M"""
        expected = """Yes
No
No
Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """4 7
2 M
3 M
1 F
4 F
4 F
1 F
2 M"""
        expected = """Yes
Yes
No
No
No
No
No"""
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
