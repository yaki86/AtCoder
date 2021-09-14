import sys
from io import StringIO
import unittest

def resolve() :
    N = int(input())
    ST = []
    for i in range(N):
        ST.append(input())

    b = 0
    for st in ST :
        if ST.count(st) >= 2:
            print("Yes")
            b = 1
            break
    if b == 0 :
        print('No')



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
tanaka taro
sato hanako
tanaka taro"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
saito ichiro
saito jiro
saito saburo"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
sypdgidop bkseq
bajsqz hh
ozjekw mcybmtt
qfeysvw dbo"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
