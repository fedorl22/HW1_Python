# Задача 2.2: - HARD необязательная, идет за 3 обязательных Найдите сумму цифр любого вещественного 
# или целого числа. Можно использовать decimal. Через строку решать нельзя. 

from decimal import Decimal


try:
    a = Decimal(input('Введите вещественное число: '))
    sum = 0
    while a % 1 != 0:
        a= a*10
        print (a)
    else:
       while a != 0:
        sum += a % 10
        a= a//10
    
    print (sum)        
except:
    print("вы ввели некорректные данные")