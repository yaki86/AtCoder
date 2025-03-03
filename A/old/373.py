import sys
import os
from io import StringIO
import unittest

def resolve():
    S = [input() for _ in range(12)]
    count = 0

    for i in range(12):
        if i+1 == len(S[i]):
            count += 1
    print(count)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """january
february
march
april
may
june
july
august
september
october
november
december"""
        expected = """1"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """ve
inrtfa
npccxva
djiq
lmbkktngaovl
mlfiv
fmbvcmuxuwggfq
qgmtwxmb
jii
ts
bfxrvs
eqvy"""
        expected = """2"""
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
