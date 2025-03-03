import sys
import os
from io import StringIO
import unittest

def resolve():
    S = [input() for _ in range(8)]
    count = 0
    start=[
        "oooooooo",
        "oooooooo",
        "oooooooo",
        "oooooooo",
        "oooooooo",
        "oooooooo",
        "oooooooo",
        "oooooooo"
    ]
    
    for i in range(8):
        if "#" in S[i]:
            start[i]="xxxxxxxx"
    for i in range(8):
        if S[0][i]==S[1][i]==S[2][i]==S[3][i]==S[4][i]==S[5][i]==S[6][i]==S[7][i]==".":
            continue
        else:
            for j in range(8):
                tmp = list(start[j])
                tmp[i]="x"
                start[j] = "".join(tmp)
    for k in range(8):
        count += start[k].count("o")
    
    print(count)

    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """...#....
#.......
.......#
....#...
.#......
........
........
..#....."""
        expected = """4"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """........
........
........
........
........
........
........
........"""
        expected = """64"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """.#......
..#..#..
....#...
........
..#....#
........
...#....
....#..."""
        expected = """4"""
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
