import sys
from io import StringIO
import unittest

def resolve():
    N,L = map(int,input().split())
    A = map(int,input().split())

    tmplist = list(filter(lambda x: x >= L,A))
    count = len(tmplist)
    print(count)

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
        input = """5 60
60 20 100 90 40"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 80
79 78 77 76"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 50
31 41 59 26 53 58 97 93 23 84"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
