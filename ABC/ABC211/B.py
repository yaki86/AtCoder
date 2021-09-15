import sys
from io import StringIO
import unittest

def resolve():
    S = []
    for i in range(4):
        S.append(input())
    result = 'Yes'
    if (S.count('2B') != 1) or (S.count('3B') != 1) or (S.count('HR') != 1) or (S.count('H') != 1):
        result = 'No'
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
        input = """3B
HR
2B
H"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2B
3B
HR
3B"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
