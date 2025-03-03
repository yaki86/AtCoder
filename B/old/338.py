import sys
from io import StringIO
import unittest

def resolve():
    S = input()
    slist = list(S)
    slist.sort()
    sdict = {}
    maxcount = 0
    maxc =""
    
    for i in range(len(slist)):
        sdict[i] = S.count(slist[i])
        if maxcount < S.count(slist[i]):
            maxcount = S.count(slist[i])
            maxc = slist[i]
    
    print(maxc)



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
        input = """frequency"""
        output = """e"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """atcoder"""
        output = """a"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """pseudopseudohypoparathyroidism"""
        output = """o"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
