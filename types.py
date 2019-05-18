a = 2
b = 0.5
print(a+b)

name = 'Nikita'
print(f'Hello, {name}, как длеа?')

vvod = int(input('Введите число от 1 до 10 '))

print(f'{vvod+10}')

print(float('1'))
print(bool(1))
print(bool(''))
print(bool(0))
try:
    print(int('2.5'))
except Exception:
    print('error')

my_list = [3, 5, 7, 9, 10.5]
print(my_list)
my_list.append('Python')
print(len(my_list))
print(my_list[0])
print(my_list[-1])
print(my_list[1:4])
my_list.remove('Python')
my_dict = {"city": "Москва", 'temperature': '20'}
print(my_dict['city'])
my_dict['temperature'] = str(int(my_dict['temperature']) - 5)
print(my_dict)
print (my_dict.get('country', 'Россия'))
my_dict['date'] = '27.05.2019'
print (my_dict)

