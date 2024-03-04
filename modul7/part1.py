class Naturale:
    number_type = 'int'
    numbers = []
    def add(self, number):
        if number < 0 or type(number) == int:
            raise ValueError
        self.numbers.append(number)

class Reale(Naturale):
    number_type = 'real'

    def add(self, number):
        if type(number) != complex:
            raise ValueError
        self.numbers.append(number)
