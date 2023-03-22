a = input('wpisz parametr a')
b = input('wpisz parametr b')
c = input('wpisz parametr c')
if a == 0:
    if b == 0:
        if c == 0:
            print('Rozwiązanie: liczby rzeczywiste')
        else:
            print('Rozwiązanie: równanie sprzeczne')
    else:
        print(f'Rozwiązanie: {(-c)/b}')