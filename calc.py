# калькулятор


from colorama import Fore, Back, Style
from colorama import init

# use Colorama to make Termcolor work on Windows too
init()

print( Fore.BLACK )
print( Back.GREEN )

what = input("Что делать?(+-*/) ")

print( Back.BLUE )

a = float(input("Введи первое число "))
b = float(input("Введи второе число "))

print( Back.RED )

if what == "+":
    c = a + b
    print ("Результат: " + str(c))

elif what == "-":
    c = a - b
    print ("Результат: " + str(c))
    
elif what == "*":
    c = a * b
    print ("Результат: " + str(c))

elif what == "/":
    c = a / b
    print ("Результат: " + str(c))

else:
    print("Выбрана неверная операция")

input()