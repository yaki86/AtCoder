import sys
from io import StringIO
import unittest

def resolve():
    S = input()
    if S == 'Hello,World!' :
        print('AC')
    else :
        print('WA')

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
        input = """Hello,World!"""
        output = """AC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """Hello,world!"""
        output = """WA"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """Hello!World!"""
        output = """WA"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
