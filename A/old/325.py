import sys
from io import StringIO
import unittest

def resolve():
    S,T = input().split()
    print(S + " san")


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
        input = """Takahashi Chokudai"""
        output = """Takahashi san"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """K Eyence"""
        output = """K san"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
