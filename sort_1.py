num = int(input())
import random
string = ""      #создание пустого списка
a = list(range(num)) #ввод размера массива
random.shuffle(a)   #перемешивание массива
for b in a:
    string += (" | " + str(b))
print(string)


def ids(n1, n2):
    if n1 > n2:
        s = a.pop(n1)
        a.insert(n2, s)
        print(a)


for number in a:
    index = a.index(number)
    for number_2 in a:
        index_2 = a.index(number_2)
        ids(index, index_2)







