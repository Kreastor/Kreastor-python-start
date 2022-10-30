# HI, world
print("HI, world")

# result:  7 15 .
print("result: ", 7,15,".")

# убираем пробелы с помощью sep (result: 715.)
print("result: ", 7,15,".", sep="")

# укзываем отсутвстие переноса принту с помощью end (First line Second line)
print("First line", end=" ")
print("Second line")

# математические операции (10)
print(5+5)

# функция min (result: -5)
print("min result:", min(5,5,7,2,4,-5,25,3))

# функция max (result: 25)
print("max result:", max(5,5,7,2,4,-5,25,3))

# функция pow (result: 25)
print("pow result:", pow(5,2))

# функция round (result: 2)
print("round result:", round(5/2))

# получение данных от пользователя (аналог prompt у js)
a = input("Укажите свой возраст: ")

print(a)