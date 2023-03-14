n = int(input())
vse = set(range(1,n+1))
b = vse
while n > 0:
    ask = input()
    if ask == 'HELP':
        break
    ask = {int(i) for i in ask.split()}
    ask &= b
    if len(ask) <= n/2:
        print ('NO')
        b -= ask
        n = n - len(ask)
    else:
        print('YES')
        b = ask
        n = len (ask)
for elem in list(b):
    print (elem, end=' ')