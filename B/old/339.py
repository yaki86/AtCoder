import sys
from io import StringIO
import unittest

def resolve():
    H,W,N = map(int,input().split())
    ans = [["."]*W for i in range(H)]
    point = [0,0]
    dir = 1
    # 1:up, 2:right, 3:down, 4:left

    for i in range(N):
        if ans[point[0]][point[1]] == '.':
            ans[point[0]][point[1]] = '#'
            if dir == 4:
                dir = 1
            else:
                dir += 1
        else:
            ans[point[0]][point[1]] = '.'
            if dir == 1:
                dir = 4
            else:
                dir -= 1
        
        if dir==1:
            if point[0] == 0:
                point[0] = H-1
            else:
                point[0] -= 1
        elif dir ==2:
            if point[1] == W-1:
                point[1] = 0
            else:
                point[1] += 1
        elif dir ==3:
            if point[0] == H-1:
                point[0] = 0
            else:
                point[0] += 1
        elif dir ==4:
            if point[1] == 0:
                point[1] = W-1
            else:
                point[1] -= 1

    for i in range(H):
        print("".join(ans[i]))

        

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
        input = """3 4 5"""
        output = """.#..
##..
...."""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2 1000"""
        output = """..
.."""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 10"""
        output = """##........
##........
..........
..........
..........
..........
..........
..........
..........
#........#"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
