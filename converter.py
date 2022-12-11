from data import data


class Converter:
    def __init__(self, user_value, choices):
        self.user_value: float = user_value
        self.choices: dict = choices
        self.data: dict = data

    def calculate(self) -> float:
        if self.choices['in'] == self.choices['out']:
            return self.user_value
        else:
            result = self.data[self.choices['in']][self.choices['out']] * self.user_value
            return result

    def reverse_calculate(self) -> float:
        if self.choices['in'] == self.choices['out']:
            return self.user_value
        else:
            result = self.user_value / self.data[self.choices['out']][self.choices['in']]
            return result
