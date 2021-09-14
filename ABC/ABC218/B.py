import sys
from io import StringIO
import unittest

def resolve():
    tmp = input().split()
    P = []
    for p in tmp:
        P.append(int(p))

    S = ""
    start = 'abcdefghijklmnopqrstuvwxyz'

    for t in P :
        S += start[t-1]

    print(S)



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26"""
        output = """abcdefghijklmnopqrstuvwxyz"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26"""
        output = """bacdefghijklmnopqrstuvwxyz"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 11 12 16 25 17 18 1 7 10 4 23 20 3 2 24 26 19 14 9 6 22 8 13 15 21"""
        output = """eklpyqragjdwtcbxzsnifvhmou"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
