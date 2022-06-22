# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.


param = ['Prefix','AD/Metric','Next-Hop','Last update','Outbound Interface']
with open('ospf.txt', 'r') as f:
    for line in f:
        for paramm in param:
            print(f'{paramm:<25}{line.split()[1]}')
"""
param = ['Prefix','AD/Metric','Next-Hop','Last update','Outbound Interface']

with open('ospf.txt', 'r') as f:
    for line in f:
        value = line.replace("[", " ").replace("]", " ").replace(",", " ").split()
        print(("{:25}{}\n"*5).format(param[0],value[1],
                                   param[1],value[2],
                                   param[2],value[4],
                                   param[3],value[5],
                                   param[4],value[6]
                                   ))

