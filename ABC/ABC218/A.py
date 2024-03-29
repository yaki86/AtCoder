import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    s = input()
    if s[N-1] == 'o':
        print('Yes')
    else :
        print('No')

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
oooxoox"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
ooooooo"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
