import random

header = "nume,VGL,MCF,RLCI,CERPA"
family_names = "Popescu,Ionescu,Stanescu,Popa,Dumitru,Stoica,Mihai,Andrei,Radu,Marin,Vasile,Gheorghe,Andreescu,Tudor," \
               "Diaconu,Pop,Munteanu,Dobre,Luca,Petrescu,Nistor,Dumitrescu,Moldovan,Florea,Ciobanu,Nicolae,Marinică," \
               "Oprea,Constantinescu,Ionita,Neagu,Sandu,Barbu,Stoian,Preda,Stefanescu,Mihaila,Manole,Radulescu," \
               "Dobrin,Serban,Rosu,Olaru,Sava,Fodor,Iacob,Ilie,Toma,Enache"


def generate_data():
    file = open('data.csv', 'w', encoding='utf-8')
    file.write(header + '\n')

    for name in family_names.split(','):
        VDAE = random.randint(0, 100000)
        VGL = random.randint(VDAE, VDAE*2)
        MCF = random.randint(VDAE, VGL)-VDAE
        RLCI = VGL - MCF - VDAE
        CERPA = random.randint(0, 20000)

        data = f'{name},{VGL},{MCF},{RLCI},{CERPA}'

        print(data)

        file.write(data + '\n')


def generate_full_data():
    file = open('data.csv', 'w', encoding='utf-8')
    file.write(header + '\n')

    for vdae in range (1, 101):
        for cerpa in range (1, 21):
            name = f'familie{str(vdae)}-{str(cerpa)}'

            VDAE = vdae*1000
            CERPA = cerpa*1000


            VGL = random.randint(VDAE, VDAE * 2)
            MCF = random.randint(VDAE, VGL) - VDAE
            RLCI = VGL - MCF - VDAE

            data = f'{name},{VGL},{MCF},{RLCI},{CERPA}'

            print(data)

            file.write(data + '\n')
