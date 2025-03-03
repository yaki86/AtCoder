import sys
from io import StringIO
import unittest

def resolve():
    N, Q = map(int, input().split())
    list = []
    for i in range(Q):
        H,T=input().split()
        list.append([H, int(T)])

    count = 0
    L = 1
    R = 2
    
    for i in range(Q):
        if list[i[0]]=="L" and list[i[1]]==L:
            continue
        elif 
    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """6 3
R 4
L 5
R 6"""
        expected = """8"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """100 2
L 1
R 2"""
        expected = """0"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """30 8
R 23
R 26
R 29
L 20
R 29
R 19
L 7
L 16"""
        expected = """92"""
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
    resolve()
