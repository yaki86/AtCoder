import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    S = input()
    lose = S.index('1')
    if lose % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

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
        input = """5
00101"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
010"""
        output = """Aoki"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
