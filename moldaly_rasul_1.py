class Animals:
    def __init__(self, name, size,  color ):
        self.name = name
        self.size = size
        self.color = color

    def __str__(self):
        return \
        f'name: {self.name}\n' \
        f'size: {self.size}\n' \
        f'color:{self.color}\n' \

bear = Animals(name='bear', size=1.0,color='brown')

print(bear)

class Birds(Animals):
    def __init__(self, name, size, color,  wingspan, predator, sing, show):
        super().__init__(name, size, color)
        self.wingspan = wingspan
        self.predator = predator
        self.sing = sing
        self.show = show

    def __str__(self):
        return super(Birds, self).__str__()+\
            f'Wingspan: {self.wingspan}\n' \
            f'Predator(yes|no): {self.predator}\n' \
            f'Sing(yes|no): {self.sing}\n' \
            f'Show: {self.show}\n'

parrot = Birds(name='Попугай', size=0.2,  color='радужные цвета', wingspan='20 см', predator='no', sing='yes', show='повторять за человеком')

print(parrot)

class Reptloid(Animals):
    def __init__(self, name, size, color, predator, show):
        super().__init__(name, size, color)
        self.predator = predator
        self.show = show

    def __str__(self):
        return super(Reptloid, self).__str__()+   f'Predator(yes|no): {self.predator}\n' \
                                                  f'Show: {self.show}\n'


crockodail = Reptloid(name='крокодил', size=1.5, color='creen', predator='yes', show='показывать дрессированное выступление' )

print(crockodail)


class Zoo_show:
    def __init__(self, zoo):
        self.zoo = zoo
        self.ticket = 0
        if zoo.name == 'Попугай':
            self.ticket = '10 $'
        if zoo.name == 'крокодил':
            self.ticket = '25 $'


    def cost(self):
        return f'Шоу будет стоить: {self.ticket}'

    def __str__(self):
        return f'{self.zoo.name} будет {self.zoo.show}'


test1 = Zoo_show(crockodail)
print(test1.cost())
print(test1)
print('-'*40)
test2 = Zoo_show(parrot)
print(test2.cost())
print(test2)