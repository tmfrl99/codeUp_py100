h, w = map(int, input().split())
n = int(input())
li = [[0 for j in range (w+1)] for i in range (h+1)]

for i in range (n):
    l, d, x, y = map(int, input().split())

    if d == 0:
        for j in range(l):
            li[x][y+j] = 1
    else:
        for j in range(l):
            li[x+j][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(li[i][j], end=' ')
    print()