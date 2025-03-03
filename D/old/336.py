import sys
from io import StringIO
import unittest

def resolve():
    import math
    N = int(input())
    A = list(map(int,input().split()))
    print(A)

    while(True):
        for i in range(math.floor((N+1)/2)):
            if A[i] < i+1:
                A.pop(-1)
                print(A)
                break
        break

    while(True):
        for i in range(math.floor((N+1)/2)-1,N,1):
            if A[i] < (N+1)/2+i:
                A.pop(0)
                print(A)
                break
        break
    print(len(A))


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
2 2 3 1 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 2 3 4 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1000000000"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
