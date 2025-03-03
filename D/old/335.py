import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    mapping = [[0 for i in range(N)] for j in range(N)]
    x = 0
    y = 0
    dx = 1
    dy = 0
    
    for i in range(N**2-1):
        mapping[-y][x]=i+1
        x += dx
        y += dy
        if dx == 1:
            if x == N-1 or mapping[-y][x+1] != 0:
                dx = 0
                dy = -1
                continue
        if dy == -1:
            if -y == N-1 or mapping[-y+1][x] != 0:
                dx = -1
                dy = 0
                continue        
        if dx == -1:
            if x == 0 or mapping[-y][x-1] != 0:
                dx = 0
                dy = 1
                continue
        if dy == 1:
            if -y == 0 or mapping[-y-1][x] != 0:
                dx = 1
                dy = 0
                continue
    mapping[int((N+1)/2)-1][int((N+1)/2)-1]="T"
    for i in range(N):
        print(" ".join([f'{i}' for i in mapping[i]]))


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
        input = """5"""
        output = """1 2 3 4 5
16 17 18 19 6
15 24 T 20 7
14 23 22 21 8
13 12 11 10 9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

