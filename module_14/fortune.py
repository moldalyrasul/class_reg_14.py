from random import choice


class Fortune:
    def game(self, bid):
        self.result = 0
        mythical = ["Дракон", "Кентавр", "Грифон"]
        random = choice(mythical)
        question = choice(mythical)

        answer = input(f"За дверью стоит {question}?")
        if bid > 0:
            if answer == "верю" and random == question or answer == "не верю" and random != question:
                print(f"За двербю стоял {random}")
                self.result = bid * 2
                print(f"Вы победили! Ваш выигрыш теперь равен: {self.result}$")
            if answer == "верю" and random != question or answer == "не верю" and random == question:
                print(f"За двербю стоял {random}")
                self.result = 0
                print(f"Вы победили! Ваш выигрыш теперь равен: {self.result}$")
        elif bid < 0:  # если проигрывали и вы в минусе
            if answer == "верю" and random == question or answer == "не верю" and random != question:
                print(f"За двербю стоял {random}")
                self.result = 0
                print(f"Вы победили! Ваш проигрыш теперь равен: {self.result}$")
            if answer == "верю" and random != question or answer == "не верю" and random == question:
                print(f"За двербю стоял {random}")
                self.result = bid * 2
                print(f"Вы проиграли! Ваш проигрыш теперь равен: {self.result}$")