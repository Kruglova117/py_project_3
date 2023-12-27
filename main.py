
start = int(input("Ведіть перше число: "))
end = int(input("Введіть друге число: "))
sum = 0
count = 0

for i in range(start, end+1):
    sum += i
    count += 1
ang = sum/count
print("Сума чисел", sum)
print("Середнє арифметичне", ang)








