import sys
from io import StringIO
import unittest

def resolve():
    tmp = input()
    X = []
    result = 'Strong'
    for i in range(4):
        X.append(int(tmp[i]))

    if X.count(X[0]) == 4:
        result = 'Weak'
    else:
        for i in range(3):
            if X[i] == 9 and X[i+1] != 0:
                break
            if X[i] != 9 and X[i+1] != X[i] + 1:
                break
            if i == 2:
                result = 'Weak'
    print(result)

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
        input = """7777"""
        output = """Weak"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0112"""
        output = """Strong"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9012"""
        output = """Weak"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
