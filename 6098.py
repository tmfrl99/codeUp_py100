d = [[0 for j in range (11)] for i in range (11)]
x = 2
y = 2

for i in range(10):
    a = list(map(int,input().split()))
    for j in range(10):
        d[i+1][j+1] = a[j]

while True:
    if d[x][y] == 0:
        d[x][y] = 9
        
    elif d[x][y] == 2:
        d[x][y] = 9
        break

    if d[x+1][y] == 1 and d[x][y+1] == 1:
        break

    if d[x][y+1] != 1:
        y += 1
    else:
        x += 1
print()
for i in range(1, 11):
    for j in range(1, 11):
        print(d[i][j], end=' ')
    print()