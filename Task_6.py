n = int(input())
s = set()
for i in range(n):
    s.update(input().split())
print(len(s))
