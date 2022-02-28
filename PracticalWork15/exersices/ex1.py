from random import uniform as u


def solve():
    print("Задание:\n 1. В матрице элементы первого столбца возвести в куб\n")

    while True:
        n = input("Введите размерность матрицы (через пробел высота и ширина > 0): ")
        n, m = n.split() if n.count(" ") > 0 else ("", "")
        if n.isdigit() and m.isdigit() and int(n) * int(m) > 0:
            m = int(m)
            n = int(n)
            break
        else:
            print("Некорректные данные\n")

    matrix = [
        [
            round(u(0, 25), 2) 
                for _ in range(m)
        ] 
        for __ in range(n)
    ]

    print("Начальная матрица: ")
    print(*matrix, sep='\n')

    print("\nИзменённая матрица: ")
    print(
        *[
            [
                round(matrix[i][j]**3, 2) 
                    for j in range(len(matrix[i]))
            ] 
                for i in range(len(matrix))
        ], 
        sep='\n'
    )
    print()