lit=input('Introduceti litera: ')
vocale=('a', 'e', 'i', 'o', 'u','ă','â','î','A','E','O','I','U','Ă','Î', 'Â')
consoane=('b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'ț', 'v', 'w', 'x', 'z', 'y','ș','Ș','B', 'C', 'D', 'F', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'Ț', 'V', 'W', 'X', 'Z', 'Y')
if lit in vocale:
    print(lit, 'este vocala')
elif lit in consoane:
    print(lit, 'este consoana')
else:
    print('Eroare')