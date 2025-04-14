order_amount = [100, 200, None, "invalid", 300, 100.5]

sum = 0
for i in order_amount:
    if type(i) == int or type(i) == float:
        sum = sum + i
    else:
        continue
print(sum)