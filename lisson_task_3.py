side = input("Укажите длину стороны квадрата в см:") 
side = float(side)
def square(side):
    print(float(side) **2)
square(side)

import math
num = float(side) **2
rounded_num = math.ceil(num)
print(rounded_num)
