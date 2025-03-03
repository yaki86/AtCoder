import sys
from io import StringIO
import unittest

def resolve():
    import math
    N = int(input())
    log = math.log2(N)
    # print(log)
    ceil = math.ceil(log)
    # print(ceil)
    anslist = []
    answer = 0

    for i in range(ceil+1):
        anslist.append(0)

    while(N>1):
        log = math.log2(N)
        #print(log)
        ceil = math.ceil(log)
        #print(ceil)
        anslist[-ceil-1] = 1
        print(anslist)
        N -= 2**(ceil-1)
        #print(N)

    anslist.reverse()

    for i in range(len(anslist)):
        #print(anslist)
        answer += anslist[i]*2**(i)
        #print(answer)

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
        input = """8"""
        output = """24"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """133"""
        output = """2024"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31415926535"""
        output = """2006628868244228"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
