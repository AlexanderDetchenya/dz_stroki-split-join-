#Разделить строку “Apples, Oranges, Pears, Bananas, Berries” по запятым и вывести на экран. Затем объединить элементы с использованием пробела, чтобы программа вывела “Apples Oranges Pears Bananas Berries”.
stroka = str('Apples, Oranges, Pears, Bananas, Berries')
print(stroka)
print(stroka.split(','))
stroka2 = stroka.split(', ')
print(' '.join(stroka2))