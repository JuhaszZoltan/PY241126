szoveg:str = "xoxoxoxoxo"
# uj_szoveg = szoveg.replace('x', 'y')

# "remove" helyett:
uj_szoveg:str = szoveg.replace('x', '')

print(uj_szoveg)
uj_szoveg = "xy" + uj_szoveg

if uj_szoveg.startswith('xy'):
    print('xy-al kezdődik')
else: print('nem xy-al kezdődik')