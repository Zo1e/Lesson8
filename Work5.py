class Warehouse:
    def __init__(self, name, price, quantity, times):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.warehouse = []
        self.full_warehouse = []
        self.times = times
        self.l_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def main(self):
        try:
            unit = input(f'Введите название - ')
            unit_p = int(input(f'Введите цену за единицу товара - '))
            unit_q = int(input(f'Введите кол-во товара - '))
            unique = {'Модель устройства': unit, 'Цена за единицу': unit_p, 'Количество': unit_q}
            self.l_unit.update(unique)
            self.warehouse.append(self.l_unit)
            print(f'Список товара на складе - {self.warehouse}')
        except:
            return f'Неверно введены данные'

        print(f'Для выхода - X, продолжение - Enter')
        x = input()
        if x == 'X' or x == 'x':
            self.full_warehouse.append(self.warehouse)
            print(f'Весь склад - {self.full_warehouse}')
            return f'Выход'
        else:
            return Warehouse.main(self)

class Printer(Warehouse):
    def print(self):
        return f'Напечатать что-то {self.times} раз'


class Scanner(Warehouse):
    def scan(self):
        return f'Сканировать что-то {self.times} раз'


class Copier(Warehouse):
    def copy(self):
        return f'Скопировать что-то {self.times} раз'


unit_1 = Printer('Hewlett-Packard', 3000, 5, 15)
unit_2 = Scanner('Samsung', 1400, 3, 12)
unit_3 = Copier('Xiaomi', 900, 2, 9)
print(unit_1.main())
print(unit_2.main())
print(unit_3.main())
print(unit_1.print())
print(unit_3.copy())