############## Algebra Liniowa - Python - 29.10.26 ###################

##### Wazne paczki #####
import numpy as np                  # biblioteka jezyka Python sluzaca do wykonywania obliczen numerycznych, szczegolnie na wektorach, macierzach i tablicach wielowymiarowych.

##### Przydatne skroty #####
# ctrl + /   - sluzy do wykomentowania zaznaczonej czesci kodu

########################################################################################################################
##### 1] Podstawy - Tworzenie Macierzy w Python #####
print("##### 1] Podstawy - Tworzenie Macierzy w Python #####", "\n")

### 1.1 Tworzenie Macierzy
# Tworzenie Macierzy 2x2
matrix = np.array([[1, 2],[3, 4]])
print("Macierz 2x2: \n", matrix, "\n")

# Tworzenie Macierzy 3x3
matrix = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print("Macierz 3x3: \n", matrix, "\n")

# Tworzenie Macierzy 3x2
matrix = np.array([[1, 2],[3, 4],[5, 6]])
print("Macierz 3x2: \n", matrix, "\n")

# Tworzenie Macierzy 2x3
matrix = np.array([[1, 2, 3],[4, 5, 6]])
print("Macierz 2x3: \n", matrix, "\n")


### 1.2 Tworzenie Wektorow
# Wektor poziomy
matrix = np.array([[1, 2, 3]])
print("Wektor poziomy: \n", matrix, "\n")

# Wektor pionowy
column_vector = np.array([1, 2, 3]).reshape(-1, 1)
print("Wektor pionowy: \n", column_vector)


### 1.3 Tworzenie Skalarow (pojedynczych liczb)
matrix = np.array([1])
print("Macierz z 1 elementem: \n", matrix, "\n")


### 1.4 Tworzenie Specjalnych Macierzy
# Macierz Zerowa
square_matrix = np.zeros((10, 10))
print("Macierz zerowa: \n", square_matrix, "\n")

# Macierz Jedynkowa
square_matrix = np.ones((3, 3))
print("Macierz jedynkowa: \n", square_matrix, "\n")

# Macierz Identycznosci
identity_matrix = np.identity(3)
print("Macierz identycznosci: \n", identity_matrix, "\n")

# Macierz Diagonalna
diagonal_matrix = np.diag([1, 2, 3])
print("Macierz diagonalna: \n", diagonal_matrix, "\n")



# ########################################################################################################################
# ##### 2] Podstawowe Dzialania i Operacje na Macierzach w Python #####
print("##### 2] Podstawowe Dzialania i Operacje na Macierzach w Python #####", "\n")

### 2.1 Wypisywanie elementow macierzy
# Wypisywanie elementu wektora
arr = np.array([1,2,3])
print("Wypisz element macierzy o indexie 1: ", arr[1], "\n")

# Wypisywanie elementow wektora po pewnej liczbie
arr = np.array([1,2,3])
print("Wypisz elementy macierzy zaczynajac od elementow o indexie 1: ", arr[1:], "\n")

# Wypisywanie elementow Macierzy
matrix = np.array([[1, 2],[3, 4]])
print("Wypisz element lezacy w 2 wierszu w 2 kolumnie: ", matrix[1, 1], "\n")

# Wyciaganie wierszy/kolumn
matrix = np.array([[1, 2],[3, 4]])
print("Cala macierz: ", matrix, "\n")

# Rows
print("Wypisz 1 wiersz: ", matrix[0, :], "\n")
print("Wypisz 2 wiersz: ", matrix[1, :], "\n")

# Columns
print("Wypisz 1 kolumne: ", matrix[:, 0], "\n")
print("Wypisz 2 kolumne: ", matrix[:, 1], "\n")


### 2.2 Podstawowe Dzialania na Macierzach
# Dodawanie Macierzy
matrix1 = np.array([[1, 2],[3, 4]])
matrix2 = np.array([[5, 6],[7, 8]])
print("Wypisz wynik dodawania dwoch macierzy: \n", matrix1 + matrix2, "\n")

# Mnozenie Macierzy
matrix1 = np.array([[1, 2, 3],[4, 5, 6],[1, 2, 3]])
matrix2 = np.array([[7, 8, 9],[10, 11, 12],[7, 8, 9]])
print("Wypisz wynik mnozenia dwoch macierzy kwadratowych: \n", np.dot(matrix1, matrix2), "\n")


matrix1 = np.array([[1, 2, 3],[4, 5, 6]])
matrix2 = np.array([[7, 8],[9, 10],[11, 12]])
print("Wypisz wynik mnozenia dwoch macierzy: \n", np.dot(matrix1, matrix2), "\n")

# Mnozenie Macierzy razy skalar
matrix = np.array([[1, 2], [3, 4]])
skalar = 2
print("Wypisz wynik mnozenia macierzy razy skalar: \n", matrix * skalar, "\n")

# Transpozycja Macierzy
matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print("Wypisz wynik transpozycji macierzy 3x3: \n", matrix.T, "\n")

# Skrotowe mnozenie Macierzy
matrix1 = np.array([[1, 2],
                   [3, 4]])

matrix2 = np.array([[2, 3],
                   [4, 5]])

print("Wynik mnozenia odpowiadajacych sobie elementow w dwoch macierzach: \n", matrix1 * matrix2, "\n") # Udawane mnozenie - mnoza sie odpowiadajace sobie elementy
print("Wynik skroconego zapisu mnozenia macierzy: \n", matrix1 @ matrix2, "\n")                         # Poprawne mnozenie Macierzy


### 2.3 Pozostale

# Wymiar macierzy
matrix = np.array([[1, 2],[3, 4],[5, 6]])
rows, cols = matrix.shape
print(f"Wymiary macierzy: {rows} rows, {cols} columns")

# Czy wymiary Macierzy sa rowne
matrix1 = np.array([[1, 2],[3, 4]])
matrix2 = np.array([[1, 2],[3, 4]])
matrix3 = np.array([[1, 2],[3, -1]])
print("Czy macierz nr 1 i 2 sa rowne? : \n", np.array_equal(matrix1, matrix2))
print("Czy macierz nr 1 i 3 sa rowne? : \n", np.array_equal(matrix1, matrix3))


# ########################################################################################################################
##### 3] Wlasciwosci Operacji na Macierzach w Python #####

print("##### 3] Wlasciwosci Operacji na Macierzach w Python #####", "\n")

# Nieprzemiennosc mnozenia macierzy
matrix1 = np.array([[1, 2], [4, 5]])
matrix2 = np.array([[2, 4], [6, 8]])
print("Wynik mnozenia matrix1 @ matrix2:\n", matrix1 @ matrix2, "\n")
print("Wynik mnozenia matrix2 @ matrix1:\n", matrix2 @ matrix1, "\n")

# Mnozenie macierzy z lewej strony - skalowanie wierszy
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
L = np.array([[2, 0, 0], [0, 3, 0], [0, 0, 4]])
print("Wynik mnozenia macierzy L @ matrix (skalowanie wierszy):\n", L @ matrix, "\n")

# Mnozenie macierzy z prawej strony - skalowanie kolumn
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
R = np.array([[2, 0, 0], [0, 3, 0], [0, 0, 4]])
print("Wynik mnozenia macierzy matrix @ R (skalowanie kolumn):\n", matrix @ R, "\n")

# Mnozenie przez macierz jednostkowa
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
I = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print("Wynik mnozenia macierzy przez macierz jednostkowa:\n", matrix @ I, "\n")

# Obracanie kolejnosci wierszy i kolumn
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
O = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
print("Wynik mnozenia matrix @ O (zmiana kolejnosci kolumn):\n", matrix @ O, "\n")
print("Wynik mnozenia O @ matrix (zmiana kolejnosci wierszy):\n", O @ matrix, "\n")

# Mnozenie przez nietypowa macierz
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
N = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
print("Wynik 1 mnozenia macierzy przez nietypowa macierz N:\n", matrix @ N, "\n")

# Mnozenie przez nietypowa macierz
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
N = np.array([[1, 0, 0], [0, 0, 1], [0, 0, 0]])
print("Wynik 2 mnozenia macierzy przez nietypowa macierz N:\n", matrix @ N, "\n")

