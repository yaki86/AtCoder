import sys
import os
from io import StringIO
import unittest

def resolve():
    S = input()
    
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    point = S.find("A")
    count = 0

    for i in range(len(S)-1):
        count += abs(S.find(alp[i+1])-point)
        point = S.find(alp[i+1])
    
    print(count)

    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
        expected = """25"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """MGJYIZDKSBHPVENFLQURTCWOAX"""
        expected = """223"""
        self.judge(input, expected)

    def judge(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    if "ATCODER" in os.environ:
        resolve()
    else:
        unittest.main(verbosity=2)
