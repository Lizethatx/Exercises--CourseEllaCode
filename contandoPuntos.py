categoriesPunctuation = list(map(int, input().split()))

if all(0 <= punctuation <= 10 for punctuation in categoriesPunctuation):
    R = sum(categoriesPunctuation)
    print(R)
else:
    print("Error: Todas las puntuaciones deben estar entre 0 y 10.")
