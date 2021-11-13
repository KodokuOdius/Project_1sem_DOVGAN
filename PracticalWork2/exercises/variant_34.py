
def solve():

    print("========> Ответ <========")
    print("Даны целые положительные числа A, B, C.\n" +
            "На прямоугольнике размера A х B размещено максимально возможное количество\n" +
            "квадратов со стороной C (без наложений).\n" +
            "Найти количество квадратов, размещенных на прямоугольнике,\n" +
            "а также площадь незанятой части прямоугольника")

    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    c = int(input("Введите C: "))

    if ( a * b ) < ( c * c ):
        return print("Невозможно разместить квадрат")

    print("========> Ответ <========")
    print(f"Количество квадратов, размещенных на прямоугольнике - { ( a*b ) // ( c*c ) }\n" + 
            f"Площадь незанятой части прямоугольника - { ( a*b ) % ( c*c ) }")
