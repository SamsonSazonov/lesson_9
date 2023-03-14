C,D =[int(i) for i in input().split()]
A,B=set(),set()
for i in range(C):
    A.add(int(input()))
for i in range(D):
    B.add(int(input()))
def show(sset):
    print(len(sset))
    print(*[str(i) for i in sorted(sset)])
show(A&B)
show(A-B)
show(B-A)
