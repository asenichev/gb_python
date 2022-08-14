"""5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
должен разместиться после них."""

some_list = [7, 5, 3, 3, 2]
print(f"Рейтинг: {some_list}")
entered_int = int(input("Введите число "))
# Запускаем цикл
# Если при переборе элементов списка в (пределах количества элементов):
for i in range(len(some_list)):
    # Один из них совпадает с введенным целым числом
    if some_list[i] == entered_int:
        # result_list.insert(pos, entered_int) Разместить на следующей после pos (индекс элемент списка) позиции элемент
        # entered_int
        some_list.insert(i + 1, entered_int)
        break
    # Если значение первого элемента списка меньше введенного целого числа
    elif some_list[0] < entered_int:
        # result_list.insert(pos, entered_int) Разместить на позиции pos (индекс элемента списка) элемент
        # entered_int
        some_list.insert(0, entered_int)
        break
    # Если значение последнего элемента списка больше введенного целого числа
    elif some_list[-1] > entered_int:
        # result_list.append(entered_int) Добавить элемент entered_int в конец списка some_list
        some_list.append(entered_int)
        break
    # Если значение введенного целого числа меньше одного значения элемента в списке, но больше другого
    elif some_list[i] > entered_int > some_list[i + 1]:
        # result_list.insert(pos, entered_int) Разместить на слудеющей позиции pos (индекс элемента списка) элемент
        # entered_int. Работает для значения, отсутствующего в списке
        some_list.insert(i + 1, entered_int)
        break
print(f"Обновленный список - {some_list}")
