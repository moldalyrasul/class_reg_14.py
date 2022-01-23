class Noob:
    def __init__(self, name, experience, skill, speed, selfcontrol):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('The name should be string!')
        if isinstance(skill, str):
            self.ex = experience
        else:
            raise ValueError('The experience should be string!')
        if isinstance(skill, str):
            self.skill = skill
        else:
            raise ValueError('The skill should be string!')
        if isinstance(speed, str):
            self.speed = speed
        else:
            raise ValueError('The speed should be string!')
        if isinstance(selfcontrol, str):
            self.slc = selfcontrol
        else:
            raise ValueError('The selfcontrol should be string!')

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Experience: {self.ex}\n' \
               f'Skill: {self.skill}\n' \
               f'Speed: {self.speed}\n' \
               f'Selfcontrol: {self.slc}\n' \

    def crying(self, crying):
        return f'He often loves {crying}'

    def foullanguage(self, foullanguage):
        return f'He also loves to use {foullanguage}\n'

class OrdinaryGamer(Noob):
    def __init__(self, name, experience, skill, speed, selfcontrol):
        super().__init__(name, experience, skill, speed, selfcontrol)

    def gentleness(self, gentle):
        return f'He can be {gentle}'

    def communication(self, talking):
        return f'He can keep a good {talking}\n'

    def __str__(self):
        return super(OrdinaryGamer, self).__str__()


class ProGamer(Noob):
    def __init__(self, name, experience, skill, speed, selfcontrol):
        super().__init__(name, experience, skill, speed, selfcontrol)

    def secrets(self, places):
        return f'He know all secret {places}'

    def money(self, cash):
        return f'He has a lot of {cash}\n'

    def __str__(self):
        return super(ProGamer, self).__str__()

class Cheater(OrdinaryGamer, ProGamer):
    def __init__(self, name, experience, skill, speed, selfcontrol):
        super().__init__(name, experience, skill, speed, selfcontrol)

    def unfair(self, cheats):
        return f'He uses {cheats}, so he is unfair'

    def bad(self, spoils):
        return f'He plays unfairly, so he {spoils} all the fun of other gamers\n'
    
    def __str__(self):
        return super(Cheater, self).__str__()


noobik = Noob('Ержан', 'Low', 'Low', 'Pre-intermediate', 'Low')
normal = OrdinaryGamer('Мирсаид', 'Intermediate', 'Intermediate', 'Intermediate', 'Intermediate')
profi = ProGamer('Серик', 'High', 'High', 'High', 'High')
cheater = Cheater('Олег', 'Immeasurable', 'Immeasurable', 'Immeasurable', 'Immeasurable')

print(noobik)
print(noobik.crying('crying'))
print(noobik.foullanguage('foul language'))
print(normal)
print(normal.gentleness('gentle'))
print(normal.communication('talking'))
print(profi)
print(profi.secrets('places'))
print(profi.money('cash'))
print(cheater)
print(cheater.unfair('cheats'))
print(cheater.bad('spoils'))
print('_'*50)

class Pizza:
    def __init__(self, name, size, taste, price):
        self.name = name
        self.size = size
        self.taste = taste
        self.price = price

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Size: {self.size}\n' \
               f'Taste: {self.taste}\n' \
               f'Price: {self.price}\n'

    def Hot(self, hot):
        return f'The pizza is {hot}'

    def Cheesy(self, cheesy):
        return f'The pizza is very {cheesy}\n'


class Pepperoni(Pizza):
    def __init__(self, name, size, taste, price):
        super().__init__(name, size, taste, price)

    def Pork(self, pork):
        return f'The pizza contains {pork}'

    def RedPepper(self, paprika):
        return f'The pizza contains {paprika}\n'

    def __str__(self):
        return super(Pepperoni, self).__str__()


class Margherita(Pizza):
    def __init__(self, name, size, taste, price):
        super().__init__(name, size, taste, price)

    def Tomatoes(self, tomatoes):
        return f'The pizza contains a lot of {tomatoes}'

    def Mozzarella(self, mozzarella):
        return f'The pizza contains {mozzarella}\n'

    def __str__(self):
        return super(Margherita, self).__str__()


class Hawaiian(Pizza):
    def __init__(self, name, size, taste, price):
        super().__init__(name, size, taste, price)

    def Pineapples(self, pineapples):
        return f'The pizza contains many {pineapples}'

    def Chicken(self, chicken):
        return f'The pizza contains many bits of {chicken}\n'

    def __str__(self):
        return super(Hawaiian, self).__str__()

pizza_1 = Pizza('Kebab', 'Small', 'Hot', '$3')
pizza_p = Pepperoni('Pepperoni', 'Medium', 'Tasty', '$5')
pizza_m = Margherita('Margherita', 'Medium', 'Yummy', '$7')
pizza_h = Hawaiian('Hawaiian', 'Big', 'Delicious', '$15')


print(pizza_1)
print(pizza_1.Hot('hot'))
print(pizza_1.Cheesy('cheesy'))
print(pizza_p)
print(pizza_p.Pork('pork'))
print(pizza_p.RedPepper('paprika'))
print(pizza_m)
print(pizza_m.Tomatoes('tomatoes'))
print(pizza_m.Mozzarella('mozzarella'))
print(pizza_h)
print(pizza_h.Pineapples('pineapples'))
print(pizza_h.Chicken('chicken'))
print('_'*50)

class CinemaTheatre:
    def __init__(self, movie):
        self.movie = movie
        self.price = 0

        if self.movie == 'Cube':
            self.price += 260
        if self.movie == 'Брат':
            self.price += 100
        if self.movie == 'Mortal Kombat':
            self.price += 300

    def __str__(self):
        return f'You chose film: {self.movie}\n' \
               f'Ticket price: ${self.price}\n'

movie_1 = CinemaTheatre("Cube")
print(movie_1)
print('_'*50)

class Starbucks:
    def __init__(self, name):
        self.name = name

    def name_of_coffee(self, name):
        if len(name) >= 9:
            return f'Your {name[0:5]} in {self.name}!'
        else:
            return f'Your {name} in {self.name}!'

    def __str__(self):
        return f'You chose coffee: {self.name}'

es = Starbucks('Espresso')
print(es)
print(es.name_of_coffee('Nicko Norton'))