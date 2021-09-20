def max (x, y):
    if x> y:
        return x
    else:
        return y

x = float(input('Число 1: '))
y = float(input('Число 2: '))

print(max (x, y))



def hello(name):
    '''Коментарий к функции'''
    print('Hi '+ name() + ' !') 

def read():
    return '___' + input ('Введите ваше имя: ') + '___'


hello (read)