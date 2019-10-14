sum1 = 0
a = 1
b = 2
c = 0
while(a<=4000000):
    c = a+b
    a = b
    b = c
    if a % 2 == 0:
        sum1 += a
print(sum1)
