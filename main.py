start = int(input("Початок діапазон: "))
end = int(input("Кінець діапазону: "))

for i in range(start, end+1):
    if i % 3 == 0:
        print("Fizz")

    if i % 5 == 0:
        print("Buzz")

    if i % 3 ==0 and i % 5==0:
        print("Fizz Buzz")

    if i % 3 !=0 and i % 5 !=0:
        print(i)
else:
    print("done")







