test = [1,4,6,8]  # Список

w = 1

while w <=10:   #До 10
    if w in test:  # Если в списке
        print (str(w) + ' В списке')
        w += 1
    else:
        print (str(w) + ' Нет в списке')
        w += 1



p  = [2,5,77,9,4,5,456]

p.append(6) # Добавить в конец списка
print ('В масиве у на ' + str(len(p)) + ' элементов')# печатает len номер в списке
print (p)


p.remove(5) # удалить элемент из списка
p.sort() # отсортировать список
print ('В масиве у на ' + str(len(p)) + ' элементов')
print (p)

p.reverse () #развернуть список
print (p)

print  (min(p)) #минимум и максимум из списка
print ( 'у меня в списке ' + str(p.count(4)) + ' четверка') #проверка сколько заданных значенйи в списке



i = list(range (50, 61, 3)) #с чего начат, до скольки, с каким шагом

print (i)


q =[11,21,31,41,51]
o = 0
lol = len(q) - 1

while o <= lol:
    print ( str(q[o]) + '!')
    o += 1

for elem in q:
    print (str(elem) + ' добавим')

for test in range(15):
    print ('hell ' + str(test))