# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
file = "config_sw1.txt"
file2 = "result.txt"


with open(file) as f, open(file2, 'w') as result:
    for line in f:
        words = line.split()
        words_intersect = set(words).intersection(set(ignore))
        if not line.startswith("!") and not words_intersect:
            result.writelines((line.rstrip())+"\n")

print(file2)