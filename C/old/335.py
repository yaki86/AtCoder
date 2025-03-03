import sys
from io import StringIO
import unittest

'''
Python など、deque に対する添字アクセスが高速でない言語では、
配列をリバースし「先頭の要素を取り除く」処理を実際には行わないことで、すべての処理を高速に行うことができます。
https://atcoder.jp/contests/abc335/editorial/9026

insertしていくと、O(NQ)の処理。appendでも同じだが、、、
実際はinsert と append で大きな速度差。
（2221ms vs 395ms）
insertで配列の先頭に要素を追加する形だと、配列のi番目を探す処理で時間がかかっているという解釈。

appendで配列の最後に追加する分にはあまり時間かからないらしい。

'''


def resolve():

    import sys
    input = sys.stdin.readline
    N,Q = map(int,input().split())
    query = [list(map(str,input().split())) for q in range(Q)]
    parts = []

    for i in range(N,0,-1):
        parts.append([i,0])

    for q in range(Q):
        if query[q][0] == "2":
            print(f'{parts[-int(query[q][1])][0]} {parts[-int(query[q][1])][1]}')
        else:
            if query[q][1] == "R":
                parts.append([parts[-1][0]+1,parts[-1][1]])
            elif query[q][1] == "L":
                parts.append([parts[-1][0]-1,parts[-1][1]])
            elif query[q][1] == "U":
                parts.append([parts[-1][0],parts[-1][1]+1])
            else:
                parts.append([parts[-1][0],parts[-1][1]-1])


'''
Insertだと特に速度改善せず。        
        if query[q][0] == "2":
            print(f'{parts[int(query[q][1])-1][0]} {parts[int(query[q][1])-1][1]}')
        else:
            if query[q][1] == "R":
                parts.insert(0,[parts[0][0]+1,parts[0][1]])
            elif query[q][1] == "L":
                parts.insert(0,[parts[0][0]-1,parts[0][1]])
            elif query[q][1] == "U":
                parts.insert(0,[parts[0][0],parts[0][1]+1])
            else:
                parts.insert(0,[parts[0][0],parts[0][1]-1])
'''

'''
    for q in range(Q):
        if query[q][0] == "2":
            print(f'{parts[int(query[q][1])-1][0]} {parts[int(query[q][1])-1][1]}')
        else:
            for i in range(N-1,0,-1):
                parts[i][0] = parts[i-1][0]
                parts[i][1] = parts[i-1][1]
            if query[q][1] == "R":
                parts[0][0] += 1
            elif query[q][1] == "L":
                parts[0][0] -= 1
            elif query[q][1] == "U":
                parts[0][1] += 1
            else:
                parts[0][1] -= 1
'''


'''
            old = copy.deepcopy(parts)
            if query[q][1] == "R":
                parts[0][0] += 1
            elif query[q][1] == "L":
                parts[0][0] -= 1
            elif query[q][1] == "U":
                parts[0][1] += 1
            else:
                parts[0][1] -= 1                
            for i in range(1,N,1):
                parts[i] = old[i-1]
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
        input = """5 9
2 3
1 U
2 3
1 R
1 D
2 3
1 L
2 1
2 5"""
        output = """3 0
2 0
1 1
1 0
1 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
