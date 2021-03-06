# Вариант 6. 
# 1. Даны температуры за месяц март. Необходимо найти количество положительных 
# и  отрицательных  значений  температур  в  месяце,  
# самую  низкую  и  самую  высокую температуры, 
# а также среднемесячное значение температуры. 

# 2.  Составить  генератор  (yield),  
# который  переведет  символы  строки  из  верхнего 
# регистра в нижний.


def weatherPrase():
<<<<<<< HEAD
    wTOKEN = "4b734d044b0e17fb41f586befa454084"
=======
    #from settings import wTOKEN
    wToken = "4b734d044b0e17fb41f586befa454084"
    
>>>>>>> ee94004a938143d97e1b8791d103d9e5c6bb5947
    data = __import__("requests").get(
        "http://api.openweathermap.org/data/2.5/forecast",
        params={
            "q": "Rostov",
            "units": "metric",
            "lang": "ru",
            "APPID": wTOKEN
        }
    ).json()
    
    temp_list = {idx["dt_txt"]: float(idx["main"]["temp"]) for idx in data["list"]}

    print("Прогноз температуры на 5 дней:")
    for dt in temp_list:
        print(
            f"🌡 {dt} = {temp_list[dt]} ℃"
        )


def ex1():
    march_temp_2021 = {
        '1': '+4°', '2': '+4°', 
        '3': '+5°', '4': '+7°', 
        '5': '+8°', '6': '+2°', 
        '7': '+2°', '8': '+5°', 
        '9': '+3°', '10': '0°', 
        '11': '-4°', '12': '-3°', 
        '13': '+2°', '14': '+8°', 
        '15': '+10°', '16': '+9°', 
        '17': '+13°', '18': '+6°', 
        '19': '+7°', '20': '+7°', 
        '21': '+6°', '22': '+7°', 
        '23': '+5°', '24': '+3°', 
        '25': '+2°', '26': '+3°', 
        '27': '+10°', '28': '+10°', 
        '29': '+11°', '30': '+5°', 
        '31': '+13°'
    }
    print("Все данные:")
    for day in march_temp_2021.keys():
        print(
            f"{day} = {march_temp_2021[day]}"
        )
    print()
    pos = sum([1 for i in march_temp_2021.values() if "+" in i])
    print(f"Кол-во положительных значений = {pos} ℃")
    neg = sum([1 for i in march_temp_2021.values() if "-" in i])
    print(f"Кол-во отрицательных значений = {neg} ℃")
    temp = [int(t[:-1]) for t in march_temp_2021.values()]
    print(f"Самая низкая температура в месяце =  {min(temp)} ℃")
    print(f"Самая высокая температура в месяце = {max(temp)} ℃")
    print(f"Среднемесячная температура = {round(sum(temp)/len(temp), 2)} ℃")


def ex2():

    def Yfunc(sent):
        yield sent.lower()

    text = input("Введите текст:\n")

    text = list(Yfunc(text))

    print("Новый текст:")
    print(*text)


    
while True:

    ex = input("Вариант 6. Выберите (0 - выход) задание: ")

    if ex == "0":
        print("Выход из программы")
        break

    elif ex == "1":
        while True:

            task = input("(0 - выход)\nПрогноз температуры на 5 дней (= 1) или решение задания (= 2) ?: ")
            if task == "0":
                break

            elif task == "1":
                weatherPrase()
                break

            elif task == "2":
                print("Условие:")
                print(
                    "Вариант 6.\n" +
                    "1. Даны температуры за месяц март.\n"
                    "Необходимо найти количество положительных\n" +
                    "и  отрицательных  значений  температур  в  месяце,\n" +
                    "самую  низкую  и  самую  высокую температуры,\n" +
                    "а также среднемесячное значение температуры."
                )
                ex1()
                break

            else:
                print("Внимательнее!")


    elif ex == "2":
        print("Условие:")
        print(
            "2.  Составить  генератор  (yield),\n" +
            "который  переведет  символы  строки\n" +
            "из  верхнего регистра в нижний."
        )
        ex2()

    else:
        print("Нет такого задания")
