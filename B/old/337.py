import sys
from io import StringIO
import unittest

def resolve():
    S = list(input())
    state = "A"
    answer = "Yes"

    for i in range(len(S)):        
        if state =="A" and S[i] == "A":
            continue
        elif state=="A" and S[i]=="B":
            state = "B"
        elif state=="A" and S[i]=="C":
            state = "C"
        elif state=="B" and S[i]=="B":
            continue
        elif state =="B" and S[i]=="C":
            state = "C"
        elif state == "C" and S[i]=="C":
            continue
        else:
            answer = "No"
    
    print(answer)



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
        input = """AAABBBCCCCCCC"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ACABABCBC"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """A"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """ABBBBBBBBBBBBBCCCCCC"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
