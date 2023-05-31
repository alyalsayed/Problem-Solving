MAXX = 1000000
d = [0] * (MAXX + 1)

def sieve():
    for i in range(1, MAXX + 1):
        for j in range(i, MAXX + 1, i):
            d[j] += 1

sieve()
n = int(input())
for _ in range(n):
    x = int(input())
    print(d[x])
