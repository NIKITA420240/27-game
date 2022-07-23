mas = [3001,3989,8999,9973]
f = open('27-ое задание 2.txt')
n = int(f.readline()) # Считываем n
k = 0 # Обнуляем переменную, которая считает количество простых чисел
for i in range(n): # в форе перебираем число х, если оно равно любому из чисел в массиве, тогда k += 1
    x = int(f.readline())
    flag = False
    for j in range(4):
        if x == mas[i]:
            flag = True
    if flag == True:
        k += 1
print(k)
