import sys
from io import StringIO
import unittest
import math

def resolve():
    N = int(input())
    NB = bin(N)
    
    tmp = len(str(NB))-2
    ans = N * (tmp-1)

    for i in range(tmp):
        if NB[i] == "1" and i != 0:
            ans += 2**(tmp-i)
    
    print(ans)

'''
    list = []
    list.append(int(input()))
    ans = 0
    i=0
    while(True):
        if i == len(list):
            break
        if list[i] > 1:
            ans += list[i]
            list.append(math.floor(list[i]/2))
            list.append(math.ceil(list[i]/2))
            list.remove(list[i])
            i = 0
        else:
            i += 1
    
    print(ans)
'''

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
        input = """3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """340"""
        output = """2888"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000000000000000"""
        output = """5655884811924144128"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
