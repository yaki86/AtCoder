import sys
from io import StringIO
import unittest
import copy

def resolve():
    N = int(input())
    QA = list(map(int,input().split()))
    QB = copy.copy(QA)
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    hello


'''
    flag1 = True
    flag2 = True
    flag3 = True
    flag4 = True

    Acount = 0
    Bcount = 0

    while(flag1):
        for i in range(N):
            if A[i] > QA[i]:
                flag1 = False
                break
        if flag1:
            for i in range(N):
                QA[i] -= A[i]
        if flag1:
            Acount += 1

    while(flag2):
        for i in range(N):
            if B[i] > QA[i]:
                flag2 = False
                break
        if flag2:
            for i in range(N):
                QA[i] -= B[i]
        if flag2:
            Acount += 1

    while(flag3):
        for i in range(N):
            if B[i] > QB[i]:
                flag3 = False
                break
        if flag3:
            for i in range(N):
                QB[i] -= B[i]
        if flag3:
            Bcount += 1

    while(flag4):
        for i in range(N):
            if A[i] > QA[i]:
                flag4 = False
                break
        if flag4:
            for i in range(N):
                QB[i] -= A[i]
        if flag4:
            Bcount += 1

    print(max(Acount,Bcount))
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
        input = """2
800 300
100 100
200 10"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
800 300
100 0
0 10"""
        output = """38"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
800 300
801 300
800 301"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10
1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000
0 1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1 0"""
        output = """222222"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
