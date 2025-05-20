class IntegerToRoman:
    def __init__(self, num):
        self.num = num

    def get_roman(self):
        values = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        result = ''
        num = self.num
        for value, symbol in values:
            while num >= value:
                result += symbol
                num -= value
        return result

number = int(input("Enter an integer: "))
roman_converter = IntegerToRoman(number)
print(roman_converter.get_roman())