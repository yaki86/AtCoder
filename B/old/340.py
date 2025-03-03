import sys
from io import StringIO
import unittest

def resolve():
    Q = int(input())
    query = [list(input().split()) for i in range(Q)]
    A = []

    for i in range(Q):
        if query[i][0] == "1":
            A.append(query[i][1])
        else:
            print(A[-int(query[i][1])])


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
        input = """5
1 20
1 30
2 1
1 40
2 3"""
        output = """30
20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
