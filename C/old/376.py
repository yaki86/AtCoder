import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    Ain = list(map(int, input().split()))
    Bin = list(map(int, input().split()))
    A = sorted(Ain, reverse=True)
    B = sorted(Bin, reverse=True)
    answer = 0
    flag = 0
    count = 0

    for i in range(N-1):
        if A[i] > B[i]:
            answer = A[i]
            count += 1
            B.insert(i,answer)
            if A[-1] > B[-1]:
                print(-1)
                flag = 1
                exit
            
    if count == 1 and flag == 0: 
        print(answer)
    elif count == 0:
        print(A[N])
    elif count > 1:
        print(-1)


    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4
5 2 3 7
6 2 8"""
        expected = """3"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """4
3 7 2 5
8 1 6"""
        expected = """-1"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """8
2 28 17 39 57 56 37 32
34 27 73 28 76 61 27"""
        expected = """37"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    resolve()
