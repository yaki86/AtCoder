import sys
from io import StringIO
import unittest

def resolve() :
    s = input().split()
    if int(s[0]) > int(s[1]):
        print("Bat")
    else:
        print("Glove")


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
        input = """300 100"""
        output = """Bat"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """334 343"""
        output = """Glove"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
