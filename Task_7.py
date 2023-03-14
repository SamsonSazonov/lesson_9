n = int(input())
ai = input()
a = set(ai.split())
while ai != 'HELP':
    if input() == 'YES':
        a &= set(ai.split())
    else:
        a -= set(ai.split())
    ai = input()

print(' '.join(list(a)))
