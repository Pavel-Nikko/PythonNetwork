# -*- coding: utf-8 -*-
"""
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt.
Имя файла передается как аргумент скрипту.

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Вывод должен быть без пустых строк.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Пример вывода:
$ python task_7_2.py config_sw1.txt
Current configuration : 2033 bytes
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
hostname sw1
interface Ethernet0/0
 duplex auto
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 duplex auto
 spanning-tree portfast edge trunk
interface Ethernet0/2
 duplex auto
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100"
 duplex auto
 switchport mode trunk
 spanning-tree portfast edge trunk
...

"""

from sys import argv
print(argv)
file = "config_sw1.txt"
with open(file) as f:
    print(file)
    for line in f:
        a = line.replace("!", " ").rstrip()
        if len(a) != 0:
           print(a)

