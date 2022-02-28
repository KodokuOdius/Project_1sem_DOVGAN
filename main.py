# Вариант 6.
# 1. В матрице элементы первого столбца возвести в куб.
# 2. Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.

from random import uniform as u

def ex1():
    n = input("Размерность матрицы (через пробел высота и ширина > 0): ")
    n, m = n.split()

    matrix = [[round(u(0, 25), 2) for j in range(int(m))] for i in range(int(n))]

    print("Начальная матрица: ")
    print(*matrix, sep='\n')

    print("Изменённая матрица: ")
    print(*[[round(matrix[i][j]**3, 2) for j in range(len(matrix[i]))] for i in range(len(matrix))], sep='\n')

def ex2():
    n = input("Размерность матрицы (через пробел высота и ширина > 0): ")
    n, m = n.split()

    matrix = [[round(u(0, 25), 2) for j in range(int(m))] for i in range(int(n))]
    print("Начальная матрица: ")
    print(*matrix, sep='\n')

    print("Изменённая матрица: ")
    print(*[[matrix[i][j] if matrix[i][j] < 10 else 0 for j in range(len(matrix[i]))] for i in range(len(matrix))], sep='\n')

