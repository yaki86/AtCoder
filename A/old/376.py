import sys
from io import StringIO
import unittest

def resolve():
    A, B = map(int, input().split())
    l = list(map(int, input().split()))
    ame = 0
    time = 0

    for i in range(A):
        if  i == 0:
            ame += 1
            time = l[i]
        elif l[i] - time >= B:
            ame += 1
            time = l[i]
    print(ame)


class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """6 5
1 3 7 8 10 12"""
        expected = """3"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """3 2
0 2 4"""
        expected = """3"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """10 3
0 3 4 6 9 12 15 17 19 20"""
        expected = """7"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
