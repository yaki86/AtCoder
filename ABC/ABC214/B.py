import sys
from io import StringIO
import unittest

def resolve():
    tmp = input().split()
    S = int(tmp[0])
    T = int(tmp[1])
    count = 0
    a = 0
    b = 0
    c = 0
    for a in range(max(S,T) + 1):
        b = 0
        c = 0
        if (a + b + c <= S) and (a * b * c <= T):
            a
        else:
            break
        for b in range(max(S,T) + 1):
            c = 0
            if (a + b + c <= S) and (a * b * c <= T):
                b
            else:
                break
            for c in range(max(S,T) + 1):
                if (a + b + c <= S) and (a * b * c <= T):
                    count += 1
                else:
                    break
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
        input = """1 0"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10"""
        output = """213"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """30 100"""
        output = """2471"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
