a, b, c = map(int, input().split(' '))
print((a if a<b else b) if a<c else (c if c<b else b))