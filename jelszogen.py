from random import randint

# karakterek:str = 'abcdefgh1234567890_'
# jelszo = ''
# for _ in range(8):
#     jelszo += karakterek[randint(0, len(karakterek)-1)]

# print(jelszo)

specs:str = '_:?,.-*>;~^#&@{}[]()+!%/='

for x in range(10):
    jelszo:str = ''
    for _ in range(12):
        rnd = randint(0, 99)
        match rnd:
            case rnd if rnd < 20:
                jelszo += specs[randint(0, len(specs)-1)]
            case rnd if rnd < 40:
                jelszo += chr(randint(65, 90))
            case rnd if rnd < 100:
                jelszo += chr(randint(97, 122))
    print(f'{x}.: {jelszo}')
