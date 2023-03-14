n, k = [int(s) for s in input().split()]

dz = set()
for i in range(k):
    a, b = [int(s) for s in input().split()]
    s = 0
    j = 0
    while s < n:
        s = a + j*b
        j += 1
        if (s % 7 in range(1, 6) and s <= n):
            dz.add(s)

print(len(dz))