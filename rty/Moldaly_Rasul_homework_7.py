while True:
    string = input("Enter a letter:")
    if string == string[::-1]:
        print("Универсальное число")
    else:
        print("Не универсальные")
        break

