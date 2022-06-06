# 4*. Замените “#” на “/” в 'www.my_site.com#about '
text = str('www.my_site.com#about')
print("Ссылка", text)
vveden = input('Для того, чтобы заменить # на /, введите команду "replace", соблюдая реестр: ')
komanda = str(' replace')
komanda1 = str('replace')
if vveden == komanda or vveden == komanda1:
    text_bez = text.split('#')
    print('/'.join(text_bez))
else:
    print("Команда не распознана!")


