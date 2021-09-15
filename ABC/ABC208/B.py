import sys
from io import StringIO
import unittest
from math import factorial

def resolve():
    coin = []
    for i in range(10):
        coin.append(factorial(i+1))
    P = int(input())
    total = 0
    for j in range(9,-1,-1):
        if P == 0:
            break
        if coin[j] <= P:
            coin_count = min(P // coin[j],100)
            P -= coin_count * coin[j]
            total += coin_count
    print(total)

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
        input = """9"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """119"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000"""
        output = """24"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
