a = set()
b = list(input().split())
for i in b:
    print("YES" if (i in a) else "NO")
    a.add(i)
