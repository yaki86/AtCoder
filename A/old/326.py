import sys
from io import StringIO
import unittest

def resolve():
    X,Y = map(int, input().split())
    if X > Y :
        if X - Y <= 3:
            print("Yes")
        else:
            print("No")
    elif Y - X <= 2:
        print("Yes")
    else:
        print("No")
        

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
        input = """1 4"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """99 96"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 1"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
