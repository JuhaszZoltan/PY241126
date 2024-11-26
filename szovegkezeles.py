# stringkezeles

# árvíztűrő tükörfúrógép
# "cica" = ['c', 'i', 'c', 'a']

# nev:str = "Juhász Zoltán"
# for c in nev: print(c, ' ')

# for i in range(len(nev)):
#     print(f'{'  '*i}{nev[i]}')

# szo:str = input('irj be valamit: ')

# for _ in range(len(szo) + 2): print(end='*')
# print(f'\n*{szo}*')
# for _ in range(len(szo) + 2): print(end='*')

# for i in range(len(szo)-1, -1, -1):
#     print(end=f'{szo[i]}')

# 0 1 2 3
# C I C A ->

# for x in range(len(szo)):
#     print(szo[len(szo) - x - 1], end='')

# for x in range(len(szo)):
#     print(szo[-(x+1)], end='')

# print(szo[::-1])

# db = 0
# for c in szo.lower():
#     if c == 'e': db += 1
# print(f'e betuk szama: {db}')

# print(f'a szó csupa kisbetűvel: {szo.lower()}')
# print(f'a szó csupa nagybetűvel: {szo.upper()}')
# print(f'minden szó nagy kezdőbetűvel: {szo.title()}')
# print(f'nagy kezdőbetűvel: {szo.capitalize()}')

szoveg:str = input("irj be egy szoveget: ")
# szavak_szama = 0
# for c in szoveg:
#     if c == ' ': szavak_szama += 1
# print(f'szavak száma: {szavak_szama + 1}')
print(f'szavak száma: {len(szoveg.split())}')

match szoveg[-1]:
    case '!': print('felszólító, óhajtó vagy felkiáltó mondat')
    case '?': print('kérdő mondat')
    case '.': print('kijelentő mondat')
    case _: print('nem hagyományos mondatzáró írásjel, nem lehet eldönteni')

if 'ly' in szoveg.lower(): print('van benne "ly"')
else: print('nincs benne "ly"')

mghk:str = 'aáeéiíoóöőuúüű'

mgh_db:int = 0
for c in szoveg.lower():
    if c in mghk: mgh_db += 1
print(f'magánhangzók száma: {mgh_db}')

