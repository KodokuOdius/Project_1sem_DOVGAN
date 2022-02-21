# 6. Из  исходного  текстового  файла  (ip_address.txt)  
# из  раздела  «Зарезервированные адреса» 
# перенести в первый файл строки с ненулевыми первым и вторым октетами, 
# а  во  второй  –  все  остальные.    
# Посчитать  количество  полученных  строк  в  каждом файле.

import re

task = """
Из  исходного  текстового  файла  (ip_address.txt)  
из  раздела  «Зарезервированные адреса» 
перенести в первый файл строки с ненулевыми первым и вторым октетами, 
а  во  второй  –  все  остальные.    
Посчитать  количество  полученных  строк  в  каждом файле."""

def solve():
    if __name__ != "__main__":
        print(
            "\nУсловие:\n" +
            task
        )
    

    files = {
        "in": open("ip_address.txt", "rt", encoding="utf-8"), 
        "out1": open("_temp1.txt", "wt", encoding="utf-8"), 
        "out2": open("_temp2.txt", "wt", encoding="utf-8")
    }

    _with_two_zeros_ip = 0
    _others = 0
        
    pattern = r"((\d+\.)+[\/\d+]*)"
    result = map(lambda ip: ip[0], re.findall(pattern, files["in"].read()))

    def _with_plus():
        nonlocal _with_two_zeros_ip
        _with_two_zeros_ip += 1
        
    
    def _oth_plus():
        nonlocal _others
        _others += 1
        

    [
        print(ip, file=files["out1"]) or _with_plus()
            if ip.split(".")[:2] == ['0', '0']
        else
            print(ip, file=files["out2"]) or _oth_plus()
        for ip in result
    ]

    # The same:
    
    # for ip in result:
    #     if ip.split(".")[:2] == ['0', '0']:
    #         _with_two_zeros_ip += 1
    #         print(ip, file=files["out1"])
    #     else:
    #         _others += 1
    #         print(ip, file=files["out2"])

    print("Ответ")
    print(
        f"\n Всего: {_with_two_zeros_ip}", 
        file=files["out1"]
    )
    print(
        f"\n Всего: {_others}", 
        file=files["out2"]
    )

    print(*list(result), sep=' ')
    print(f"Всего {_with_two_zeros_ip + _others} ip-адресов")
    print(f"В первом файле (_temp1.txt) {_with_two_zeros_ip} ip-адреса")
    print(f"Во втором файле (_temp2.txt) {_others} ip-адреса")

    for file in files.values():
        file.close()



if __name__ == "__main__":
    solve()