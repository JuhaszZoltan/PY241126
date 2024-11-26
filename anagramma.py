szoveg01:str = input("ird be elso szot: ")
szoveg02:str = input("ird be masodik szot: ")


kar_list_01:list[chr] = []
for c in szoveg01.lower(): kar_list_01.append(c)
kar_list_01.sort()

kar_list_02:list[chr] = []
for c in szoveg02.lower(): kar_list_02.append(c)
kar_list_02.sort()

rendezett01:str = ''.join(kar_list_01)
rendezett02:str = ''.join(kar_list_02)

print(rendezett01)
print(rendezett02)

if rendezett01 == rendezett02:
    print('anagramma')
else: print('nem anagramma')