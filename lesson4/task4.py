"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генераторное выржаение.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

main_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# Функция .count подсчитывает количество вхождений символа/подстроки в строку.
# Синтаксис: str.count(sub[, start[, end]])
# Условие: если количество вхождений символа в строке = 1
new_list = [el for el in main_list if main_list.count(el) == 1]
print(f'{new_list}')