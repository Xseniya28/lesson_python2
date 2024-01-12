
#Первый вариант 

Lst = ["grape", "peach", "pear", "orange", "apple", "banana"]
print(Lst[0] , Lst[5])

# Второй вариант 

Lst = ["grape", "peach", "pear", "orange", "apple", "banana"]
print(Lst[0] , Lst[-1])

# Третий вариант 

Lst = ["grape", "peach", "pear", "orange", "apple", "banana"]
X = len(Lst)
list2 = Lst[X-1 : ]
print(Lst[0] , list2)