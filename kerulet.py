irsz:str = input('írj be egy irányítószámot: ')

if irsz[0] != '1':
    print('ez nem budapesti irányítószám')
else:
    print(f'az az irányítószám a {irsz[1:3]}. kerületben található')