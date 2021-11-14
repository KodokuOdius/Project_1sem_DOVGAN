
def solve():
    
    print("========> Условие <========")
    print("Скорость лодки в стоячей воде V км/ч, скорость течения реки U км/ч (U < V).\n" +
            "Время движения лодки по озеру T1 ч, а по реке (против течения) — T2 ч.\n" +
            "Определить путь S, пройденный лодкой (путь = время • скорость).\n" +
            "Учесть, что при движении против течения скорость лодки уменьшается на величину скорости течения")

    v = int(input("Введите V: "))
    u = int(input("Введите U: "))
    t1 = int(input("Введите T1: "))
    t2 = int(input("Введите T2: "))

    if u > v:
        return print("Не корректные данные")

    print("========> Ответ <========")
    print(f"Путь пройденный лодкой - { v*t1 + (v - u)*t2 } км")