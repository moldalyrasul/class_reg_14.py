class Animal:
    def __init__(self, name, size, wight, color):
        self.name = name
        self.size = size
        self.wight = wight
        self.color = color

    def __str__(self):
        return \
            f'Name: {self.name}\n ' \
            f'Size: {self.size}\n ' \
            f'Wight: {self.wight}\n ' \
            f'Color: {self.color}\n '

bear = Animal(name='Медведь', size=1.6, wight=100, color='белый')
wolf = Animal(name='Волк', size=1.2, wight=30, color='серый')
panda = Animal(name='Панда', size=2.3, wight=70, color='белая и черная')


class Birds(Animal):
    def __init__(self, name, size, wight, color, wingspan, predator, sing, show):
        super().__init__(name, size, wight, color)
        self.wingspan = wingspan
        self.predator = predator
        self.sing = sing
        self.show =show

    def __str__(self):
        return \
            f'Wingspan: {self.wingspan}\n' \
            f'Predator(yes|no): {self.predator}\n ' \
            f'Sing(yes|no): {self.sing}\n ' \
            f'Show: {self.show}\n '

eagl = Birds(name='Орел', size=0.6, wight=10, color='коричневый', wingspan='45 см', predator='yes', sing='no', show='охотиться за лисой' )
parrot = Birds(name='Попугай', size=0.2, wight=0.2, color='радужные цвета', wingspan='20 см', predator='no', sing='yes', show='повторять за человеком')
penguin = Birds(name='Пингвин', size=0.8, wight=20, color='черный', wingspan='5 см', predator='no', sing='no', show='прыгать и хлопать')

print(eagl)
print(parrot)
print(penguin)


class Zoo_show:
    def __init__(self, zoo):
        self.zoo = zoo
        self.ticket = 0
        if zoo.name == 'Попугай':
            self.ticket = '15 $'
        if zoo.name == 'Орел':
            self.ticket = '20 $'
        if zoo.name == 'Пингвин':
            self.ticket = '17 $'

    def cost(self):
        return f'Шоу будет стоить: {self.ticket}'

    def __str__(self):
        return f'{self.zoo.name} будет {self.zoo.show} '

show1 = Zoo_show(parrot)
show2 = Zoo_show(penguin)
show3 = Zoo_show(eagl)

print(show1)
print(show1.cost())
print(show2)
print(show2.cost())
print(show3)
print(show3.cost())


