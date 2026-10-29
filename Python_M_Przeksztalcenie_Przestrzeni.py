import numpy as np
import matplotlib.pyplot as plt

########################################################################################################################
# Przeksztalcenia w 2d

# 1. Wektory tworzace kwadrat jednostkowy
Kwadrat = np.array([[0, 1, 1, 0, 0],
              [0, 0, 1, 1, 0]])

# 2. Macierz przeksztalcenia
A = np.array([[2, 0],
              [0, -1]])

# 3. Przeksztalcenie kwadratu
Kwadrat_new = A @ Kwadrat

print("Wspolrzedne kwadratu po przeksztalceniu: \n", Kwadrat_new)
# 4. Obliczenie wyznacznika i pola
det_A = np.linalg.det(A)
pole = abs(det_A)

print("Macierz przeksztalcenia:")
print(A)
print("Wyznacznik macierzy/Pole nowej figury:", det_A)

# 5. Rysowanie figur
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(Kwadrat[0], Kwadrat[1], "b-o")
plt.fill(Kwadrat[0], Kwadrat[1], alpha=0.2)
plt.title("Kwadrat przed przeksztalceniem")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.gca().set_aspect("equal", adjustable="box")
plt.xticks(range(-5, 6))
plt.yticks(range(-5, 6))
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(Kwadrat_new[0], Kwadrat_new[1], "r-o")
plt.fill(Kwadrat_new[0], Kwadrat_new[1], alpha=0.2)
plt.title("Figura po przeksztalceniu")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.gca().set_aspect("equal", adjustable="box")
plt.xticks(range(-5, 6))
plt.yticks(range(-5, 6))
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid()

plt.tight_layout()
plt.show()


########################################################################################################################
# Przeksztalcenia w 3d

# 1. Wierzcholki szescianu jednostkowego
Szescian = np.array([
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1]
])

# 2. Macierz przeksztalcenia
A = np.array([[1, 0, 0],
              [0, 0, 0],
              [0, 0, 0]])

# 3. Przeksztalcenie szescianu
Szescian_new = A @ Szescian

print("Wspolrzedne szescianu po przeksztalceniu:\n", Szescian_new)

# 4. Obliczenie wyznacznika i objetosci
det_A = np.linalg.det(A)
objetosc = abs(det_A)

print("Macierz przeksztalcenia:")
print(A)
print("Wyznacznik macierzy:", det_A)
print("Objetosc nowej bryly:", objetosc)

# 5. Krawedzie szescianu
krawedzie = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# 6. Rysowanie bryl
fig = plt.figure(figsize=(12, 6))

for nr, dane, tytul, kolor in [
    (1, Szescian, "Szescian przed przeksztalceniem", "blue"),
    (2, Szescian_new, "Bryla po przeksztalceniu", "red")
]:
    ax = fig.add_subplot(1, 2, nr, projection="3d")

    for i, j in krawedzie:
        ax.plot(dane[0, [i, j]],
                dane[1, [i, j]],
                dane[2, [i, j]],
                color=kolor)

    ax.scatter(dane[0], dane[1], dane[2], color=kolor)

    ax.set_title(tytul)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)
    ax.set_box_aspect((1, 1, 1))

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.grid()

plt.tight_layout()
plt.show()
