def get_sum(one, two, delimeter ='&'):
    one = str(one)
    two = str(two)
    return f'{one}{delimeter}{two}'


word_one = 'Learn'
word_two = 'python'
sum_string = get_sum(word_one, word_two)

print(sum_string.upper())


def format_price(price):
    price = int(price)
    return f'Цена {price} руб.'


formated_price = format_price(56.24)
print(formated_price)
