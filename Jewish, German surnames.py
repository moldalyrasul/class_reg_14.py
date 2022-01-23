while 1:
    a = str(input("Enter a surname, please: "))
    Jewish = 'Goldstein, Silverstein, Schneider, Levin'
    German = 'Lutz, Schmidt, Muller'
    if a in Jewish:
        print('The surname is Jewish')
    elif a in German:
        print('The surname is German')
    elif a == 'quit':
        break
    else:
        print("Excuse me, but the surname is not found...")




