# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

inter1 = []
b = input("Введите влан:")
with open("CAM_table.txt") as src:
    for line in src:
        if len(line.split()) == 4 and line.split()[0].isdigit() and line.split()[0] ==b:
            inter = "".join(line).split()
            vlan, mac, type, port = inter
            inter1.append([int(vlan), mac, port])


    for vlan, mac, port in sorted(inter1):
        print(f'{int(vlan):<8}{mac:<20}{port}')


