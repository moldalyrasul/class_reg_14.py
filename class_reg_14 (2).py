import re


my_text = 'Vasya, 1998, vasya@gmail.com, 4000$, male* ' \
          'Adilet, 1997 adilet@intel.com, 50089750$ male* ' \
          'Aidana, 2000 aidana@yandex.ru, 890976$ female% ' \
          'Aman, 1999, aman@mail.ru, 789$ male* ' \
          'Regina 1999 regina@yahoo.ru, 69$ female% ' \
          'Lol, 6789, lol@gmail.com 9087$ none? '

"""
\d -- Он ищет подряд стоящие ЧИСЛА [0-9]
\D -- Он ищет любые , но не числа
\w -- Ищет любой алфавитный символ [A-Z a-z]
\W -- любой не алфавитный символ
\s -- Ищет пробелы
\S -- специальные символы
"""


file_path = 'demo_mock_data.txt'
result_file_path = 'results.txt'

file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()

what_search = r'[\w_-]+(?!jbullochj5)@(?!so-net)(?!intel)(?!yahoo)(?!amazon)[\w_-]+.[\w.]+'
results = re.findall(what_search, my_text_file)

for item in results:
    print(item)
    result_file.write(item + '\n')

print(f'Total results of file: {str(len(results))}')
