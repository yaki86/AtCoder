import sys
from io import StringIO
import unittest

def resolve():
    M, D = map(int,input().split())
    y, m, d = map(int, input().split())
    
    if d == D:
        if M == m :
            y += 1
            m = 1
            d = 1
        else:
            m += 1
            d = 1
    else:
        d += 1
    print(f'{y} {m} {d}')

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
        input = """12 30
2023 12 30"""
        output = """2024 1 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """36 72
6789 23 45"""
        output = """6789 23 46"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12 30
2012 6 20"""
        output = """2012 6 21"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
