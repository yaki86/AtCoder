import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    A = input().split()
    tmpA = list(A)
    first_score = 0
    second_score = 0
    for a in A:
        first_score = max(first_score,int(a))
    del tmpA[tmpA.index(str(first_score))]

    for a in tmpA:
        second_score = max(second_score,int(a))

    print(A.index(str(second_score)) + 1)
        

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
        input = """6
1 123 12345 12 1234 123456"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
3 1 4 15 9"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
