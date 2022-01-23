class MmaTrainer:
    def __init__(self,style):
        self.style = style

    def trained(self, train):
        return f'this trainer teaches {train}'

    def __str__(self):
        return f'style: {self.style}\n '


athlete1 = MmaTrainer(style='sambo')
print(athlete1)
print(athlete1.trained('throw'))
print('_'*40)

class Sportsman1(MmaTrainer):
    def __init__(self, style):
        super().__init__( style )

    def arsenal(self, ars):
        return f'его арсенал состоит из бросков: {ars}'


    def __str__(self):
        return super(Sportsman1, self).__str__()

athlete2 = Sportsman1(style='judo')
print(athlete2)
print(athlete2.arsenal('через бедро, прогиб '))

class Sportsman2(Sportsman1):
    def __init__(self, style):
        super().__init__(style)

    def __str__(self):
        return super(Sportsman2, self).__str__()

    def vin(self,args):
        return f'у него {args} выносливость'

Sportsman3 = Sportsman2(style='wresling')
print('_'*50)
print(Sportsman3)
print(Sportsman3.vin('средняя'))
print('_'*50)


class Anonim:
    def __init__(self, surname, name):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'ФИО: {self.surname} {self.name}'

test = Anonim(surname='moldaly', name='Rasul')

print(test)

class Wizard:
    def __init__(self, wizard):
        self.wizard = wizard

    def attack(self,args):
        return f' его атака {args},\n' \
               f'damage -15dm\n'

    def __str__(self):
        return f'this wizard: {self.wizard}'

class Ice_Wizard:
    def __init__(self, wizard):
        self.wizard = wizard


    def attack(self,args):
        return f' его атака {args},\n' \
               f'damage -7 dm\n'

    def __str__(self):
        return f'this wizard: {self.wizard}'


class Electro_Wizard:
    def __init__(self, wizard):
        self.wizard = wizard

    def attack(self, args):
        return f' его атака {args},\n' \
               f'damage -12dm\n'


    def __str__(self):
        return f'this wizard: {self.wizard}'

wizard1 = Wizard(wizard='fire')
wizard2 = Ice_Wizard(wizard='electro')
wizard3 = Electro_Wizard(wizard='ice')

print(wizard1)
print(wizard1.attack('огненная'))
print(wizard2)
print(wizard2.attack('ледяная'))
print(wizard3)
print(wizard3.attack('электрическая'))

class Alkashi1:
    def __init__(self, name):
        self.name = name

    def rty(self,args):
        return f' дед пьет {args}\n'

    def __str__(self):
        return f'name: {self.name}'

class Alkashi2(Alkashi1):
    def __init__(self, name):
        super().__init__(name)

    def rty(self, args):
        return f' отец пьет {args}\n'

    def __str__(self):
        return super(Alkashi2, self).__str__()


class Alkashi3(Alkashi2):
    def __init__(self, name):
        super().__init__(name)

    def rty(self, args):
        return f' сын пьет {args}\n'

    def __str__(self):
        return super(Alkashi3, self).__str__()

al1 = Alkashi1(name='Сергей')
al2 = Alkashi2(name=' Алексей')
al3 = Alkashi3(name='Матвей')
print(al1)
print(al1.rty(f'коньяк'))
print(al2)
print(al2.rty('водку'))
print(al3)
print(al3.rty('виски'))

