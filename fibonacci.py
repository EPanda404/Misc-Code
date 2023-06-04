import math

Phi = ( 1 + math.sqrt(5) ) / 2
phi = ( 1 - math.sqrt(5) ) / 2

first = 0
second = 1

for i in range(100):
    if i == 0:
        print(first)
    elif i == 1:
        print(second)
    else:        
        print(second + first)
        temp = second
        second = second + first
        first = temp
    
    print (int((Phi ** i - phi ** i) / math.sqrt(5) ))