n = int(input())
import random                                            #\
lists = ""      #создание пустого списка                  #\                
a = list(range(n)) #ввод размера массива                   #\
random.shuffle(a)   #перемешивание массива               |создание и перемешивание массива
for b in a:                                                #/
    lists += (" | " + str(b))                             #/                                                                        
print(lists)                                             #/


print(lists.split(" | "))



































