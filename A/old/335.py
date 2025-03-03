import sys
from io import StringIO
import unittest

'''
最後以外を出力して、最後に4を出力するほうがよかった
'''

def resolve():
    S = list(input())
    S[-1] = "4"
    answer = "".join(S)
    print(answer)

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
        input = """hello2023"""
        output = """hello2024"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """worldtourfinals2023"""
        output = """worldtourfinals2024"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2023"""
        output = """2024"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20232023"""
        output = """20232024"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
