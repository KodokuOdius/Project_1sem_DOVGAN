
def solve():

    print("========> Условие <========")
    print("Известно, что X кг конфет стоит A рублей.\n" + 
            "Определить, сколько стоит 1 кг и Y кг этих же конфет")

    x = float(input("Введите X: "))
    a = float(input("Введите A: "))
    y = int(input("Введите Y: "))
    
    print("========> Ответ <========")
    print(f"1 кг конфет стоит - {a/x} рублей\n" 
            + f"{y} кг конфет стоит - {a/x * y} рублей")
