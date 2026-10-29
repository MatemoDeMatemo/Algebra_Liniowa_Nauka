############## Algebra Liniowa - Python - 29.10.26 ###################

##### Wazne paczki #####
import numpy as np
import matplotlib.pyplot as plt


# ########################################################################################################################
##### 1] Rozwiazywanie Ukladow Rownan w Python #####

print("##### 41] Rozwiazywanie Ukladow Rownan w Python #####", "\n")


### 1.1 Rozwiazywanie Ukladow Rownan za pomoca Macierzy Odwrotnej
# Korzystamy ze wzoru: Ax = b -> x = A^(-1)b
# A - macierz wspolczynnikow ukladu rownan
# x - wektor niewiadomych
# b - wektor wynikow

A = np.array([[2, 3], [4, 5]])
b = np.array([[10], [18]])

print("Macierz wspolczynnikow A:\n", A, "\n")
print("Wektor wynikow b:\n", b, "\n")

# Obliczanie macierzy odwrotnej do A
A_inv = np.linalg.inv(A)
print("Macierz odwrotna do A:\n", A_inv, "\n")

# Obliczanie rozwiazania ukladu: x = A^(-1) @ b
x = A_inv @ b
print("Rozwiazanie ukladu rownan za pomoca macierzy odwrotnej:\n", x, "\n")

# Alternatywny sposob rozwiazywania ukladu rownan
# Funkcja solve() oblicza rozwiazanie bez jawnego wyznaczania macierzy odwrotnej
x = np.linalg.solve(A, b)
print("Rozwiazanie ukladu rownan za pomoca funkcji np.linalg.solve():\n", x, "\n")


### 1.2 Reczne wyznaczanie macierzy odwrotnej metoda Gaussa-Jordana
# Laczymy macierz A z macierza jednostkowa I, tworzac macierz rozszerzona [A | I].
# Nastepnie wykonujemy operacje elementarne na wierszach.
# Celem jest uzyskanie macierzy jednostkowej po lewej stronie.
# Po prawej stronie otrzymujemy wtedy macierz odwrotna A^(-1).

print("##### 1.2 Reczne wyznaczanie macierzy odwrotnej metoda Gaussa-Jordana #####", "\n")

np.set_printoptions(suppress=True)

A = np.array([[4., 1, 4],
              [3, 2, 9],
              [2, 2, 10]])

D = np.hstack((A, np.identity(3)))

print("Macierz poczatkowa A:\n", A, "\n")
print("Macierz rozszerzona [A | I]:\n", D, "\n")

# Krok 1: Uzyskanie jedynki w pierwszym wierszu i pierwszej kolumnie
D[0] = D[0] / 4

# Krok 2: Wyzerowanie elementow pod pierwszym elementem glownym
D[1] = D[1] - 3 * D[0]
D[2] = D[2] - 2 * D[0]

# Krok 3: Uzyskanie jedynki w drugim wierszu
D[1] = D[1] / 1.25

# Krok 4: Wyzerowanie elementu pod drugim elementem glownym
D[2] = D[2] - 1.5 * D[1]

# Krok 5: Uzyskanie jedynki w trzecim wierszu
D[2] = D[2] / 0.8

# Krok 6: Wyzerowanie elementow nad trzecim elementem glownym
D[0] = D[0] - 0.25 * D[1]
D[0] = D[0] + 0.2 * D[2]
D[1] = D[1] - 4.8 * D[2]

print("Macierz po wykonaniu operacji Gaussa-Jordana:\n", D, "\n")

print("Lewa czesc macierzy D - powinna byc macierza jednostkowa:\n", D[:, :3], "\n")
print("Prawa czesc macierzy D - macierz odwrotna do A:\n", D[:, 3:], "\n")

# Porownanie z wynikiem funkcji NumPy
print("Macierz odwrotna obliczona przez np.linalg.inv():\n", np.linalg.inv(A), "\n")


# ########################################################################################################################
##### 2] Macierze w Badaniu Populacji #####

print("##### 2] Macierze w Badaniu Populacji #####", "\n")

# Macierz przezywalnosci oraz rozmnazania populacji.
#
# Wiersze oznaczaja klasy wiekowe w kolejnym roku,
# a kolumny oznaczaja klasy wiekowe w obecnym roku.
#
#             Klasa 1   Klasa 2   Klasa 3
# Klasa 1:      0         0.5       0
# Klasa 2:      0.8       0         0
# Klasa 3:      0         0.9       0.7
#
# 0.5 - kazdy osobnik klasy 2 produkuje srednio 0.5 osobnika klasy 1
#       w kolejnym roku.
# 0.8 - 80% osobnikow klasy 1 przezywa i przechodzi do klasy 2.
# 0.9 - 90% osobnikow klasy 2 przezywa i przechodzi do klasy 3.
# 0.7 - 70% osobnikow klasy 3 przezywa i pozostaje w klasie 3.
#
# Zera oznaczaja brak bezposredniego wplywu danej klasy na wskazana
# klase w kolejnym roku.

M = np.array([[0, 0.5, 0],
              [0.8, 0, 0],
              [0, 0.9, 0.7]])

# Poczatkowa struktura wiekowa populacji:
# 10 osobnikow w klasie 1, 4 w klasie 2 i 2 w klasie 3.
P0 = np.array([10, 4, 2])

print("Poczatkowa struktura populacji [klasa 1, klasa 2, klasa 3]:\n", P0, "\n")

# Struktura populacji po roku
P1 = M @ P0
print("Struktura populacji po 1 roku [klasa 1, klasa 2, klasa 3]:\n", P1, "\n")

# Struktura populacji po dwoch latach
P2 = M @ P1
print("Struktura populacji po 2 latach [klasa 1, klasa 2, klasa 3]:\n", P2, "\n")

# Struktura populacji po trzech latach
P3 = M @ P2
print("Struktura populacji po 3 latach [klasa 1, klasa 2, klasa 3]:\n", P3, "\n")

# Struktura populacji po n latach
n = 3
Mn = np.linalg.matrix_power(M, n)
Pn = Mn @ P0

print("Macierz M podniesiona do potegi", n, ":\n", Mn, "\n")
print("Struktura populacji po", n, "latach:\n", Pn, "\n")

# Suma osobnikow we wszystkich klasach wiekowych
N_osobnikow = Pn.sum()
print("Laczna liczba osobnikow w populacji po", n, "latach:", N_osobnikow, "\n")


## Wykres zmian liczebnosci populacji

# Macierz przezywalnosci i rozmnazania populacji
M = np.array([[0, 0.5, 0],
              [0.8, 0, 0],
              [0, 0.9, 0.7]])

# Poczatkowa struktura wiekowa populacji
P = np.array([10, 4, 2])

# Liczba lat symulacji
n = 10

# Pusty wektor przechowujacy laczna liczebnosc populacji w kolejnych latach
v = []

for i in range(n):

    # Obliczanie struktury populacji w kolejnym roku
    P = M @ P

    # Sumowanie osobnikow ze wszystkich klas wiekowych
    N_osobnikow = round(P.sum(), 2)

    print("Rok:", i + 1, "| Struktura populacji:", P,
          "| Laczna liczba osobnikow:", N_osobnikow)

    # Dodanie liczebnosci populacji do listy wynikow
    v.append(float(N_osobnikow))

print("\nLaczna liczebnosc populacji w kolejnych latach:\n", v, "\n")


# Przygotowanie danych do wykresu
xpoints = range(1, n + 1)
ypoints = v

# Rysowanie wykresu
plt.plot(xpoints, ypoints)

# Opisy osi i tytul wykresu
plt.xlabel("Rok")
plt.ylabel("Liczba osobnikow")
plt.title("Zmiany liczebnosci populacji w czasie")

# Wyswietlenie wykresu
plt.show()
