desired_sum = int(input(' желаемая сумма: '))

class summa:
    def __init__(self, numbers: list,desired_sum: int ):
        self.numbers = numbers
        self.desired_sum = desired_sum


    def index(self):
        for i in range(len(self.numbers)):
            for n in range(i + 1, len(self.numbers)):
                if (self.numbers[i] + self.numbers[n]) == self.desired_sum:
                    return (i, n)



numbers = [2, 7, 11, 15]

for i in range(len(numbers)-1):
    if (numbers[i]+(numbers[i+1])) == desired_sum:
        print([i, i+1])

