ekezetes:str = 'áéíóöőúüűÁÉÍÓÖŐÚÜŰ'
ekmentes:str = 'aeiooouuuAEIOOOUUU'

szoveg:str = input("irj be egy szoveget: ")
ekezet_mentes_szoveg:str = ''

for c in szoveg:
    if c not in ekezetes:
        ekezet_mentes_szoveg += c
    else:
        i:int = ekezetes.index(c)
        ekezet_mentes_szoveg += ekmentes[i]

print(f'ékezetek nélkül: {ekezet_mentes_szoveg}')