import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    saving = 0
    for i in range(N):
        saving += i+1
        if saving >= N:
            print(i+1)
            break


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
        input = """12"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100128"""
        output = """447"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
