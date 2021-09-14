import sys
from io import StringIO
import unittest

def resolve():
    tmp = input().split('.')
    X = int(tmp[0])
    Y = int(tmp[1])
    if Y <= 2 :
        print('' + str(X) + '-')
    elif Y <= 6 :
        print('' + str(X))
    else :
        print('' + str(X) + '+') 

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
        input = """15.8"""
        output = """15+"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1.0"""
        output = """1-"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12.5"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
