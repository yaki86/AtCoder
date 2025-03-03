import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    XY = [list(map(int,input().split())) for i in range(N)]
    x = 0
    y = 0
    
    for i in range(N):
        x += XY[i][0]
        y += XY[i][1]
    
    if x > y :
        print("Takahashi")
    elif y > x:
        print("Aoki")
    else:
        print("Draw")




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
        input = """4
10 2
10 1
10 2
3 2"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
5 4
4 5
2 4
1 6
7 1
3 2"""
        output = """Draw"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
0 0
10 10
50 50
0 100"""
        output = """Aoki"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
