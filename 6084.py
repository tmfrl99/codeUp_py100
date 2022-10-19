h, b, c, s = map(int, input().split(' '))
mb = h*b*c*s/8/1024/1024
print(round(mb, 1), "MB")