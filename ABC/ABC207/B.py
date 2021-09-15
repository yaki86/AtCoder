import sys
from io import StringIO
import unittest
def resolve():
    A,B,C,D = map(int,input().split())
    count = 0
    '''
    A + NB <= NCD
    if B = CD , A > 0 ...x
    if CD - B > 0, then A/(CD-B) <= N ...o 
    if CD - B < 0, then 0> A/(CD-B) >= N ...x
    '''
    if C * D - B <= 0:
        print(-1)
    else:
        while(True):
            count += 1
            if A + count * B <= count * C * D:
                print(count)
                break
    

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
        input = """5 2 3 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 9 2 3"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
