import random

"""23.10"""


def suma_liczb_naturalnych_od_1_do_n(n):
    suma = 0
    for i in range(n + 1):
        suma += i
    return suma


def suma_kwadratow_liczb_od_1_do_n(n):
    suma = 0
    for i in range(n + 1):
        suma += i ** 2
    return suma


# 30.10
def absolute(n):
    if n < 0:
        return -n
    return n


def sgn(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0


def dzielenie():
    x = float(input('X: '))
    y = float(input('Y: '))
    if y != 0:
        return x / y
    return 'Division impossible'


# 6.11
def czy_nalezy(tablica, element):
    for el in tablica:
        if el == element:
            return True
    return False


def czy_zawiera(lista1, lista2):
    for el1 in lista2:
        zawiera = False
        for el2 in lista1:
            if el1 == el2:
                zawiera = True
        if not zawiera:
            return False
    return True


# Zadanie domowe
# (a) 1 2 3 4 5 6 7 8 9 10
# (b) 0 2 4 6 8 10 12 14 16 18 20
# (c) 1 4 9 16 25 36 49 64 81 100
# (d) 0 0 0 0 0 0 0 0 0 0
# (e) 0 1 0 1 0 1 0 1 0 1
# (f) 0 1 2 3 4 0 1 2 3 4
def zad1():
    a = [i + 1 for i in range(10)]
    b = [i * 2 for i in range(11)]
    c = [i ** 2 for i in range(1, 11)]
    d = [i * 0 for i in range(10)]
    e = [i % 2 for i in range(10)]
    f = [i % 5 for i in range(10)]

    print(f'a) {a}')
    print(f'b) {b}')
    print(f'c) {c}')
    print(f'd) {d}')
    print(f'e) {e}')
    print(f'f) {f}')


def ile_liczb_ujemnych_w_tablicy(tablica):
    ile = 0
    for i in tablica:
        if i < 0:
            ile += 1
    return ile


def iloczyn_elementow_tablicy(tablica):
    wynik = 1
    for i in tablica:
        wynik *= i
    return wynik


def minmax(tablica):
    mini = tablica[0]
    maxi = tablica[0]
    for i in tablica:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i
    return mini, maxi


# 13.11
def generuj(n, start, koniec):
    lista = []
    for _ in range(n):
        lista.append(random.randint(start, koniec - 1))
    return lista


def remove(napis, usuwany):
    if usuwany in napis:
        indeks = napis.index(usuwany)
        napis = napis[:indeks] + napis[indeks + len(usuwany):]
        return napis
    return napis


def remove_all(napis, usuwany):
    while usuwany in napis:
        indeks = napis.index(usuwany)
        napis = napis[:indeks] + napis[indeks + len(usuwany):]
    return napis


# 20.11
def nwd(x, y):
    while y:
        x, y = y, x % y
    return x


# zadanie a)
def znajdz_liczby_mniejsze_od_n_i_wzglednie_pierwsze_z_n(n):
    wynik = []
    for i in range(1, n):
        if nwd(i, n) == 1:
            wynik.append(i)
    return wynik


def znajdz_dzielniki(n):
    x = []
    for i in range(1, int(n / 2 + 1)):
        if n % i == 0:
            x.append(i)
    return x


def suma_dzielnikow(n):
    suma = 0
    for i in n:
        suma += i
    return suma


# zadanie b)
def znajdz_liczby_doskonale_mniejsze_od_n(n):
    liczby_doskonale = []
    for i in range(1, n):
        if i == suma_dzielnikow(znajdz_dzielniki(i)):
            liczby_doskonale.append(i)
    return liczby_doskonale


def czy_pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


# zadanie c)
def znajdz_podzielniki_liczby_n_bedace_liczbami_pierwszymi(n):
    podzielniki_pierwsze = []
    for i in znajdz_dzielniki(n):
        if czy_pierwsza(i):
            podzielniki_pierwsze.append(i)
    return podzielniki_pierwsze


def ciag_fibonacci_n_elementow(n):
    elementy = [0, 1]
    while len(elementy) < n:
        elementy.append(elementy[-1] + elementy[-2])
    return elementy


# zadanie d)
def znajdz_najwieksza_liczbe_ciagu_fibonacciego_mniejsza_od_n(n):
    ciag_do_n = ciag_fibonacci_n_elementow(n)
    while ciag_do_n[-1] > n:
        ciag_do_n.pop()
    return ciag_do_n[-1]


# zadanie e_I)
def znajdz_sume_kwadratow_ktore_dadza_n(n):
    for a in range(0, int(n ** 0.5) + 1):
        for b in range(0, int((n - a ** 2) ** 0.5) + 1):
            kwadrat_c = n - a ** 2 - b ** 2
            c = int(kwadrat_c ** 0.5)
            if c ** 2 == kwadrat_c:
                return a, b, c
    return None


# zadanie e_II)
def znajdz_wszystkie_sumy_kwadratow_ktore_daja_n(n):
    wynik = set()
    for a in range(0, int(n ** 0.5) + 1):
        for b in range(0, int((n - a ** 2) ** 0.5) + 1):
            kwadrat_c = n - a ** 2 - b ** 2
            c = int(kwadrat_c ** 0.5)
            if c ** 2 == kwadrat_c:
                wynik.add((a, b, c))
    return wynik


# 27.11
def dzielniki(n, z_ta_sama_liczba=False):
    x = []
    for i in range(1, int(n / 2 + 1)):
        if n % i == 0:
            x.append(i)
    if z_ta_sama_liczba:
        return x.append(n)
    return x


def suma_dz(n):
    suma = 0
    for i in dzielniki(n):
        suma += i
    return suma


def czesc_wspolna(x, y):
    wynik = []
    for i in x:
        for j in y:
            if i == j:
                wynik.append(j)
    return wynik


def czy_wzglednie_pierwsze(x, y):
    dzielniki_x = dzielniki(x, True)
    dzielniki_y = dzielniki(y, True)
    iloczyn = czesc_wspolna(dzielniki_x, dzielniki_y)
    return len(iloczyn) == 1 and iloczyn[0] == 1


def czy_jest_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


def znajdz_dzielniki_ktore_sa_liczbami_pierwszymi(n):
    odp = []
    dzielniki_n = dzielniki(n)
    for i in dzielniki_n:
        if czy_jest_pierwsza(i):
            odp.append(i)
    return odp


# 4.12 & 11.12
def sumaryczna_odleglosc(dom, lista_domow):
    suma = 0
    for i in range(len(lista_domow)):
        odleglosc = abs(dom - lista_domow[i])
        suma += odleglosc
    return suma


def sumaryczne_odleglosci(lista_domow):
    d = {}
    for nr_domu in lista_domow:
        d[nr_domu] = sumaryczna_odleglosc(nr_domu, lista_domow)
    return d


def minimum(d):
    # nr_min = next(iter(d))
    # wartosc_min = d[nr_min]
    # for key in d:
    #     if d[key] < wartosc_min:
    #         wartosc_min = d[key]
    #         nr_min = key
    # return nr_min
    nr_min = next(iter(d))
    for key in d:
        if d[key] < d[nr_min]:
            nr_min = key
    return nr_min


def znajdz_najlepsza_lokalizacje(lista_domow):
    d = sumaryczne_odleglosci(lista_domow)
    return minimum(d)


def licznosc_znakow_w_tekscie_a(napis):
    d = {}
    for litera in napis:
        if litera in d:
            d[litera] += 1
        else:
            d[litera] = 1
    return d


def licznosc_znakow_w_tekscie_b(napis):
    d = {}
    for litera in napis:
        if 'a' <= litera <= 'z' or 'A' <= litera <= 'Z':
            if litera in d:
                d[litera] += 1
            else:
                d[litera] = 1
    return d


def licznosc_znakow_w_tekscie_c(napis):
    d = {}
    for litera in napis.upper():
        if 'A' <= litera <= 'Z':
            if litera in d:
                d[litera] += 1
            else:
                d[litera] = 1
    return d


def licznosc_znakow_w_tekscie_d(napis):
    d = licznosc_znakow_w_tekscie_c(napis)
    najczestsza = []
    for item in d:
        if d[item] == max(d.values()):
            najczestsza.append(item)
    return najczestsza


# 18.12
def liczby_do_slownika():
    d = {}
    while True:
        n = input()
        if n == '':
            break
        if n.isnumeric():
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        else:
            print('Podaj liczbe')
    return d


def odczyt_pliku_i_liczenie_liter(plik):
    plik = open(plik).readlines()
    d = {}
    for linia in plik:
        wiersz = linia.strip()
        for letter in wiersz:
            if letter.isalpha():
                if letter in d:
                    d[letter] += 1
                else:
                    d[letter] = 1
    return d


def odczyt_pliku_wybor_i_liczenie_liczb(plik):
    plik = open(plik).readlines()
    d = {}
    for linia in plik:
        wiersz = linia.strip().split()
        for item in wiersz:
            if item.isnumeric():
                if item in d:
                    d[item] += 1
                else:
                    d[item] = 1
    return d
