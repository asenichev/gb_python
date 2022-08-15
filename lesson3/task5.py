"""5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться 
сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь 
введённых чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, 
выполнение программы завершается. Если специальный символ введён после нескольких чисел, то вначале нужно добавить 
сумму этих чисел к полученной ранее сумме и после этого завершить программу. """


# Создаем функцию
def some_func():
    sum_res = 0
    ex = False
    # Цикл для выполнения функции после нажатия Enter
    while ex == False:
        # Вводим число
        number = input('Введите числа через пробел или нажмите q(Q) для остановки: ').split()
        res = 0
        # Цикл для выполнения проверки остановки программы и сложения введенных чисел
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[i])
        sum_res = sum_res + res
        print(f'Текущая сумма {sum_res}')
    print(f'Окончательная сумма {sum_res}')


some_func()
