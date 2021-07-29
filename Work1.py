class Data:
    def __init__(self, full_date):
        self.full_date = full_date

    @classmethod
    def extract(cls, full_date):
        ex_date = full_date.split('-')
        return int(ex_date[0]), int(ex_date[1]), int(ex_date[2])

    @staticmethod
    def valid(full_date):
        val_date = full_date.split('-')
        sp_val_date = []
        i = 0
        for el in val_date:
            sp_val_date.append(int(val_date[i]))
            i += 1
            if i > 3:
                break
        if sp_val_date[0] > 31:
            return 'Неправильно указан день!'
        else:
            if sp_val_date[1] > 12:
                return 'Неправильно указан месяц!'
            else:
                if sp_val_date[2] < 0 or sp_val_date[2] > 2025:
                    return 'Неправильно указан год!'

new_date = Data('14-11-2022')
print(new_date)
print(Data.extract('2-11-2023'))
print(Data.valid('33-11-2009'))
print(Data.valid('22-14-2009'))
print(Data.valid('22-11-2030'))



