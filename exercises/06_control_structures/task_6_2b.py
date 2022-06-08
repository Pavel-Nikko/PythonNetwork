# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите IP адрес в формате x.x.x.x :")
octet = ip.split(".")
good_ip = False
while not good_ip:

    if len(ip.split(".")) != 4:
        print("Ip должен содержать 4 октета :")
        ip = input("Введите IP адрес в формате x.x.x.x :")
        good_ip = False
    else:
        for octets in octet:
            if not (octets.isdigit() and int(octets) in range(256)):
                good_ip = False
                print("Ip должен состоять из цифр в диапазоне от 0 до 255 :")
                ip = input("Введите IP адрес в формате x.x.x.x :")
    good_ip = True
else:
    if ip == "0.0.0.0":
        print("unassigned")
    elif int(ip.split(".")[0]) >= 0 and int(ip.split(".")[0]) <= 223:
        print("unicast")
    elif int(ip.split(".")[0]) >= 224 and int(ip.split(".")[0]) <= 239:
        print("multicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    else:
        print("unused")
    good_ip = True


"""

if len(ip.split(".")) != 4:
    good_ip = False
else:
    for octets in octet:
        if not (octets.isdigit() and int(octets) in range(256)):
            good_ip = False



if not good_ip:
    print("неправильный IP")
else:
    if ip == "0.0.0.0":
        print("unassigned")
    elif  int(ip.split(".")[0]) >= 0 and int(ip.split(".")[0]) <= 223:
        print("unicast")
    elif int(ip.split(".")[0]) >= 224 and int(ip.split(".")[0]) <= 239:
        print("multicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    else:
        print("unused")

"""
