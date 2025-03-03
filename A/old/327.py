import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    S = input()
    result = "No"
    for i in range(N-1):
        if S[i]=="a" and S[i+1]=="b":
            result = "Yes"
            break
        if S[i] == "b" and S[i+1] == "a":
            result = "Yes"
            break
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
        input = """3
abc"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
ba"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
atcoder"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
