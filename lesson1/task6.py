'''Если фирма отработала с прибылью, вычислите рентабельность выручки.
Это отношение прибыли к выручке.
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
'''
revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
result = revenue - costs

if result > 0:
    print(f"Результат - прибыль в размере: {result}")

    employees = int(input("Введите численность сотрудников фирмы: "))
    employees_profit = result / employees
    print(f"Прибыль фирмы в расчете на одного сотрудника = {employees_profit}")

elif result < 0:
    print(f"Результат - убыток в размере: {result}")

else:
    print("Выручка равна издержкам")