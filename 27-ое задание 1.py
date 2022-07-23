f = open('27-B.txt')
n,d = map(int,f.readline().split()) #Считываю n и d
mas = [] # создаю массив
sumc = 0 # создаю переменную сумму цифр чисел
summ = 0 # создаю переменную сумму чисел
maxsumm = # создаю переменную максимальной суммы чисел
maxsummc = 0 # создаю переменную максимальной суммы цифр чисел
for i in range(d): # Первые d чисел считываю в массив, и считаю её сумму чисел, сумму цифр чисел
    x = int(f.readline())
    p = x
    summ += x
    while p > 0:
        sumc += p % 10
        p //= 10
    mas.append(x)
maxsummc = sumc # Обновляю данные
maxsumm = summ # Обновляю данные
pr = 0
#print(mas,sumc,summ)
for i in range(n - d): # Ключевой фор
    if sumc >= maxsummc: # Обновляю максимальную сумму чисел, если сумма цифр чисел стала больше или равна maxsummc
        if sumc == maxsummc: # В случае если равенство, то нужна максимальная сумма чисел
            maxsumm = max(maxsumm,summ)
        else:
            maxsumm = summ # В случае если sumc > maxsummc, то максимальная сумма чисел должна обновиться 
        maxsummc = max(maxsummc,sumc)
    p = mas[0] # считаю сумму цифр числа первого в наборе mas
    while p > 0:
        pr += p % 10
        p //= 10
    sumc -= pr # вычитаю из sumc сумму цифр числа первого в наборе mas
    summ -= mas[0] # вычитаю из summ число, которое является первым в наборе mas
    del mas[0] # удаляю из набора первое число
    x = int(f.readline()) # считываю новое число
    mas.append(x) #заношу в массив
    summ += x # к сумме чисел прибавляю новое число
    p = x # к сумме цифр чисел прибавляю сумму цифр нового числа
    while p > 0:
        sumc += p % 10
        p //= 10
    pr = 0
    #print(mas,sumc,summ,maxsummc,maxsumm)
if sumc >= maxsummc: #Учитываю, что если последний набор подходит под условие, то его нужно проверить
    if sumc == maxsummc:
        maxsumm = max(maxsumm,summ)
    else:
        maxsumm = summ
    maxsummc = max(maxsummc,sumc)
print(maxsumm) 
    
