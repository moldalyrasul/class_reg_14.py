import re


# name
file_path = 'MOCK_DATA.txt'
result_file_path = 'name.txt'


file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()


what_searth = r"[A-Z][A-z]+\s[A-z]+\s[A-Z][A-z]+|" \
                r"[A-Z][A-z]+\s[A-Z][A-z]+|" \
                r"[A-Z][A-z]+\s\w'\D{2}\w+|" \
                r"[A-Z][A-z]+-[A-Z][A-z]+|" \
                r"[A-Z][A-z]+-[a-z]+\s\w+"
result = re.findall(what_searth, my_text_file)



for item in result:
    print(item)
    result_file.write(item + '\n')
print(f'Total results of file: {str(len(result))}')


# email
file_path = 'MOCK_DATA.txt'
result_file_path = 'email.txt'


file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()


what_searth = r'\w+@\S+'
result = re.findall(what_searth, my_text_file)



for item in result:
    print(item)
    result_file.write(item + '\n')
print(f'Total results of file: {str(len(result))}')



# fullname
file_path = 'MOCK_DATA.txt'
result_file_path = 'fullname.txt'


file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()


what_searth = r'[A-Z]+[a-z]+\w+[.]+[a-z]+[0-9]|' \
                     r"[A-Z]+[a-z]+\w+[.]+[a-z]+|" \
                     r"[A-Z]+[a-z]+[.]+[a-z]+[0-9]|" \
                     r"[A-Z]+[a-z]+[.]+[a-z]+|" \
                     r"[A-Z]+[.]+[a-z]+|" \
                     r"[A-Z]+[.]+[a-z]+[0-9]"
result = re.findall(what_searth, my_text_file)



for item in result:
    print(item)
    result_file.write(item + '\n')

# numbers
file_path = 'MOCK_DATA.txt'
result_file_path = 'numbers.txt'


file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()


what_searth = r'#\w+'

result = re.findall(what_searth, my_text_file)



for item in result:
    print(item)
    result_file.write(item + '\n')

print(f'Total results of file: {str(len(result))}')

desired_sum = int(input(' желаемая сумма: '))


class summa:
    def __init__(self, numbers: list, desired_sum: int):
        self.numbers = numbers
        self.desired_sum = desired_sum


numbers = [2, 7, 11, 15]

for i in range(len(numbers) - 1):
    if (numbers[i] + (numbers[i + 1])) == desired_sum:
        print([i, i + 1])