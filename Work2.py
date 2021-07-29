class NullDivision:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    @staticmethod
    def division(first_number, second_number):
        try:
            return(first_number / second_number)
        except ZeroDivisionError:
            return'На ноль делить нельзя!'

print(NullDivision.division(0, 100))
print(NullDivision.division(100, 0))
print(NullDivision.division(0, 0))
print(NullDivision.division(100, 100))
