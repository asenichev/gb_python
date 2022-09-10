"""3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В
его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно. Сложение.
Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение. Умножение. Создаётся общая клетка из двух. Число ячеек общей
клетки определяется как произведение количества ячеек этих двух клеток. Деление. Создаётся общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся. Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда
метод make_order() вернёт строку: *****\n*****\n**. Или, количество ячеек клетки равняется 15, количество ячеек в
ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****. Подсказка: подробный список операторов для
перегрузки доступен по ссылке. """

'''
# ****************************
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
        # self.result = result

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        # self.result = Cell(self.quantity + other.quantity)
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

        # return Cell(int(self.quantity - other.quantity))

    def __mul__(self, other):
        # self.result = Cell(int(self.quantity * other.quantity))
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        # self.result = Cell(round(self.quantity // other.quantity))
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(3)
cells2 = Cell(4)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)'''


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'({self.quantity})'

    def __add__(self, other):
        return f'Сумма клеток = {str(Cell(self.quantity + other.quantity))}'

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return f'Разность клеток = {Cell(int(self.quantity - other.quantity))}'
        return f'Разность отрицательна, поэтому операция не выполняется'

    def __mul__(self, other):
        return f'Умножение клеток = {Cell(int(self.quantity * other.quantity))}'

    def __truediv__(self, other):
        return f'Деление клеток = {Cell(round(self.quantity // other.quantity))}'

    def make_order(self, cells_count):
        row = ''
        for _ in range(int(self.quantity / cells_count)):
            row += f'{"*" * cells_count}\\n '
        row += f'{"*" * (self.quantity % cells_count)}'
        return row


print("Создаем объекты клеток")
cell1 = Cell(30)
cell2 = Cell(25)

cell3 = Cell(10)
cell4 = Cell(15)

print()

print("Складываем")
print(cell1 + cell2)

print()

print("Вычитаем")
print(cell2 - cell1)
print(cell4 - cell3)

print()

print("Умножаем")
print(cell2 * cell1)

print()

print("Делим")
print(cell1 / cell2)

print()

print("Организация ячеек по рядам")
print(cell1.make_order(5))
print(cell2.make_order(10))
