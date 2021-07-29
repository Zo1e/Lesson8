class IsDigit:
    def __init__(self, *args):
        self.new_list = []

    def check(self):
        while True:
            try:
                new_value = int(input('Введите значения через пробел - '))
                self.new_list.append(new_value)
                print(f'Список - {self.new_list}')
            except:
                print(f'Недопустимое значение.')
                choose = input('Попробовать заново? Y/N - ')
                if choose == 'Y' or choose == 'y':
                    print(example.check())
                elif choose == 'N' or choose == 'n':
                    print('Вы вышли из программы')
                else:
                    print('Программа закрыта.')

example = IsDigit(0)
print(example.check())



