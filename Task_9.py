s = int(input())
m=[]
for i in range(s):
    m.append(set())
    for j in range(int(input())):
        m[i].add(input())
evr = set.intersection(*m)
all = set.union(*m)
print(len(evr), *sorted(evr), sep='\n')
print(len(all), *sorted(all), sep='\n')
