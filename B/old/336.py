import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    count = 0
    while(N>=1):
        if N % 2 ==0:
            count += 1
            N //= 2
        else:
            break
    print(count)


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
        input = """2024"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """18"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
