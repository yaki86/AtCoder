import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    A = list(map(int,input().split()))
    ans = []
    index_dict = {v: i for i, v in enumerate(A, start=1)}  # 値からインデックスを取得する辞書
    state = index_dict[-1]
    ans.append(str(state))
    last =""
    for _ in range(N-1):
        if state in index_dict:
            ans.append(str(index_dict[state]))
            state = index_dict[state]
        else:
            last = str(i+1) 
    
    if last !="":
        ans.append(last)

    print(" ".join(ans))

'''
def resolve():
    N = int(input())
    A = list(map(int,input().split()))
    ans = []
    ans.append(str(A.index(-1)+1))
    state = A.index(-1)+1
    last =""

    for i in range(N-1):
        if state in A:
            ans.append(str(A.index(state)+1))
            state = A.index(state)+1
        else:
            last = str(i+1) 
    
    if last !="":
        ans.append(last)

    print(" ".join(ans))
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
        input = """6
4 1 -1 5 3 2"""
        output = """3 5 4 1 2 6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
-1 1 2 3 4 5 6 7 8 9"""
        output = """1 2 3 4 5 6 7 8 9 10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30
3 25 20 6 18 12 26 1 29 -1 21 17 23 9 8 30 10 15 22 27 4 13 5 11 16 24 28 2 19 7"""
        output = """10 17 12 6 4 21 11 24 26 7 30 16 25 2 28 27 20 3 1 8 15 18 5 23 13 22 19 29 9 14"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
