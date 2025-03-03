import sys
from io import StringIO
import unittest

def resolve():
    S = input()
    ans = S.istitle()

    if ans == False:
        print("No")
    else:
        print("Yes")

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
        input = """Capitalized"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """AtCoder"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """yes"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """A"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
