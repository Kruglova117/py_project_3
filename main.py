x1 = int(input("Початок діапазону: "))
x2 = int(input("Кінець діапазону: "))
x = x1 + 1


for i in range(x1, x2+1, 1):
    if i % 7 == 0:
        print(int(i))