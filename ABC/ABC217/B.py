import sys
from io import StringIO
import unittest

def resolve() :
    S = [input(), input(), input()]
    contest = ['ABC', 'ARC', 'AGC', 'AHC']
    for s in S :
        tmp = contest.index(s)
        del contest[tmp]
    print(contest[0])

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
        input = """ARC
AGC
AHC"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """AGC
ABC
ARC"""
        output = """AHC"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
