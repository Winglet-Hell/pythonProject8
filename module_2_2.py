# Ввод чисел
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Проверка на количество одинаковых чисел
if first == second == third:
    print("Все три числа равны. Количество одинаковых чисел: 3")
elif first == second or first == third or second == third:
    print("Два из трёх чисел равны. Количество одинаковых чисел: 2")
else:
    print("Нет одинаковых чисел. Количество одинаковых чисел: 0")