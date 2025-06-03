#сдесь я буду писать код для считания суммы цифр в числе

# print(sum(list(map(int, input()))))



# print("Цвета полей совпадают" if(int(input())+int(input()))%2==(int(input())+int(input()))%2 else "Цвета полей не совпадают")

# print(eval(input()))

import random
c = input()
while c != "конец игры":
    if c == "бросить кость":
        n1 = random.randint(1, 7)
        n2 = random.randint(1, 7)
        print("ДУБЛЬ " + "(" + str(n1) + " и " + str(n2) + ")" if n1 == n2 else n1 + n2)
    c = input()

# c = input()
# while c != "конец игры":
#     print(eval(c))
#     c = input()