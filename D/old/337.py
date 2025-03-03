import sys
from io import StringIO
import unittest

def resolve():
    H,W,K = input().split
    S = [input() for i in range(H)]

    

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
        input = """3 4 3
xo.x
..o.
xx.o"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 2 3
.o
.o
.o
.o"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 3 3
x..
..x
.x."""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 12 6
......xo.o..
x...x.....o.
x...........
..o...x.....
.....oo.....
o.........x.
ox.oox.xx..x
....o...oox.
..o.....x.x.
...o........"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
