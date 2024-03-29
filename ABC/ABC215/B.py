import sys
from io import StringIO
import unittest
from math import floor, log2


# def resolve() :
#     N = int(input())
#     ans = floor(log2(N))
#     print(ans)

def resolve():
    N = int(input())
    k = 0
    while(True):
        if 2**k > N:
            print(k-1)
            break
        k += 1


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
        input = """6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000"""
        output = """59"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
