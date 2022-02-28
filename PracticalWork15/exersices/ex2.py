from random import uniform as u


def solve():
    print("Задание:\n 2. Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0\n")

    while True:
        n = input("Размерность матрицы (через пробел высота и ширина > 0): ")
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
                for _ in range(int(m))
        ] 
            for __ in range(int(n))
    ]

    print("Начальная матрица: ")
    print(*matrix, sep='\n')

    print("\nИзменённая матрица: ")
    print(
        *[
            [
                matrix[i][j] if matrix[i][j] < 10 else 0 
                    for j in range(len(matrix[i]))
            ] 
                for i in range(len(matrix))
        ], 
        sep='\n'
    )
    print()