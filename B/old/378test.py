N = 2
qr = [[7,3],[4,2]]
Q = 5
td = [[1,1],[1,3],[1,4],[1,15],[2,7]]

for i in range(Q):
    for j in range(100):
        print("t:"+str(td[i][0]))
        print("d:"+str(td[i][1]))
        print("q:"+str(qr[td[i][0]-1][0]))
        print("r:"+str(qr[td[i][0]-1][1]))
        print(td[i][1]+j % qr[td[i][0]-1][0])
        if td[i][1]+j % qr[td[i][0]-1][0] == qr[td[i][0]-1][1]:
            print(td[i][1]+j)
            print("break")
            break