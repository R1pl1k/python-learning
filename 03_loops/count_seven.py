total: int = 0
count: int = 0

for i in range (1,101):
    if i%7 == 0:
        total += i
        count += 1
print(f" сумма: {total} и чисел: {count} ")