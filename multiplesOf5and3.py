sum1 = 0
for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        if i >= 1000:
            break
        sum1 += i
print(sum1)
