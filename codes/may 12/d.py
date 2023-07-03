def akko(s: str):
    if 'm' in set(s) or 'w' in set(s):
        return 0
    if not 'n' in set(s) and not 'u' in set(s):
        return 1
    aux = [1, 1]
    for i in range(2, len(s) + 1):
        if s[i - 2:i] == 'uu' or s[i - 2:i] == 'nn':
            aux.append(aux[-1] + aux[-2])
        else:
            aux.append(aux[-1])
        if len(aux) > 10:
            aux = aux[5::]
    return aux[-1]

print(akko(input()) % (10**9 + 7))