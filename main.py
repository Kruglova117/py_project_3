x1 =int(input("Початок діапазону: "))
x2 = int(input("Кінець діапазону: "))
X = x1 +1
count = 0

for i in range(x1, x2+1, 1):
    if i % 5 ==0:
        count += 1
print(count, "Числа кратні 5" )