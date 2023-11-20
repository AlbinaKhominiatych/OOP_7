"""Створіть клас Calculator, який може виконувати
операції додавання, віднімання, множення та ділення.
Кожна операція буде реалізована як метод класу.
Об'єкт класу Calculator буде функтором, що може
викликатися для виконання обраної операції."""


class Calculator:
    # сюди додати усі інші операції
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Ділити на нуль не можна!")
        return  a / b

    def __call__(self, *args, **kwargs):
        match args[0]:
            # сюди додати усі інші операції
            case "/": return self.divide(args[1], args[2])
            case _  : return "немає такої операції"

calcutate = Calculator()
print(calcutate("/", 4, 2))