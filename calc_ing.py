from pprint import pprint

my_list = ['1.txt', '2.txt', '3.txt']
result_list = []

for i in my_list:
    my_dict = {}
    with open(i, 'r', encoding='utf-8') as file:
        my_dict['Имя файла'] = i
        lines = file.readlines()
        my_dict['Количество строк'] = len(lines)
        my_dict['Содержимое файла'] = lines
        result_list.append(my_dict)

res = sorted(result_list, key=lambda x: x['Количество строк'])
pprint(res)
