import sys
import os
from io import StringIO
import unittest

def resolve():
    N = int(input())
    qr = [list(map(int, input().split())) for l in range(N)]
    Q = int(input())
    td = [list(map(int, input().split())) for l in range(Q)]

    for i in range(Q):
        q = qr[td[i][0] - 1][0]
        r = qr[td[i][0] - 1][1]
        d = td[i][1]
        
        ans = (d + (r - d) % q)

        print(ans)

    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """2
7 3
4 2
5
1 1
1 3
1 4
1 15
2 7"""
        expected = """3
3
10
17
10"""
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
