#3. Ввести предложение. Если число символов в предложении кратно 3 - добавить ! к концу строки. Вывести строку на экран.
pred = input('Введите предложение: ')
pred_spis = pred.split(' ')
print(pred_spis)
pred_spis_ob = ''.join(pred_spis)
kolichestvo_bukv = len(pred_spis_ob)
print(kolichestvo_bukv)
if kolichestvo_bukv % 3 == 0:
    print(pred + '!')
else:
    print(pred)