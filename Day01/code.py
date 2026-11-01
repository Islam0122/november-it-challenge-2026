# 1. Переменные и типы
# Создай переменные:
# name = твоё имя
# age = твой возраст
# height = твой рост
# is_student = True/False
# Выведи их одной красивой строкой:
# Name: Islam | Age: 19 | Height: 180 | Student: True
# И отдельно выведи тип каждой переменной через type().
# name = "islam"
# print(type(name))
# age = 19
# print(type(age))
# height = 1.80
# print(type(height))
# is_student = True
# print(type(is_student))
# for i in [name, age, height,is_student]:
#     print(i)
# 2. Арифметика
# Даны:
# a = 25
# b = 7
# Выведи:
# Sum:
# Difference:
# Multiplication:
# Division:
# Integer division:
# Remainder:
# Power:
# Используй операторы Python, а не готовые значения.
# a = 25
# b = 7
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

# 3. Работа со строкой
# Дана:
# text = "Python Backend Developer"
# Получить:
# Python
# Backend
# Developer
# Затем вывести:
# Длина строки
# Строку в верхнем регистре
# Строку в нижнем регистре

# text = "Python Backend Developer"
# print(text)
# print(len(text))
# print(text.upper())
# print(text.lower())
# list_text = text.split(" ")
# text_1 = list_text[0]
# print(text_1)
# print(len(text_1))
# print(text_1.upper())
# print(text_1.lower())
# text_2 = list_text[1]
# print(text_2)
# print(len(text_2))
# print(text_2.upper())
# print(text_2.lower())
# text_3 = list_text[2]
# print(text_3)
# print(len(text_3))
# print(text_3.upper())
# print(text_3.lower())

# 4. Input + casting
# Попроси пользователя ввести:
# name
# age
# salary
# age должен быть int, salary — float.
# Вывести:
# Hello, Islam!
# Next year you will be 20.
# Your salary is 62000.0
# name = input("What is your name?")
# age = int(input("How old are you?"))
# salary = float(input("What is your salary?"))
# print("Hello " + name + "!\n Next year you will be 20" + str(age+1) + "\n Your salary is "+str(salary))

# 5. Проверка возраста
# Пользователь вводит возраст.
# Программа должна вывести:
# 0–12    → Child
# 13–17   → Teenager
# 18–59   → Adult
# 60+     → Senior
# age =  int(input("Enter your age: "))
# if 0 <= age <= 12:
#     print("Child")
# elif 13 <= age <= 17:
#     print("Teenager")
# elif 18 <= age <= 59:
#     print("Adult")
# elif age > 60:
#     print("Senior")
#

# 6. Чётное / нечётное
# Пользователь вводит число.
# Например:
# Input: 17
# Output: Odd
# Input: 24
# Output: Even
# Дополнительно определить, положительное число, отрицательное или 0.
# Input_x = int(input("Input: "))
# if Input_x % 2 == 1:
#     print("Output:Odd")
# else:
#     print("Output:Even")

# 7. Максимальное из трёх
# Даны:
# a = 15
# b = 42
# c = 27
# Найди максимальное число без max().
# Потом сделай второй вариант с max().
# a = 15
# b = 42
# c = 27
# #a
# def max_a(arr:list):
#     res = 0
#     for i in arr:
#         if i > res:
#             res = i
#     return res
# print(max_a([a,b,c]))
# #b
# print(max(a,b,c))

# 8. Система оценок
# Пользователь вводит балл от 0 до 100.
# Результат:
#
# 90–100 → A
# 80–89  → B
# 70–79  → C
# 60–69  → D
# 0–59   → F
# Если число находится вне диапазона — вывести:
# Invalid score

# score = int(input("Enter your score:"))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# elif score >= 0:
#     print("F")
# else:
#     print("Invalid score")
#

# 9. Числа от 1 до 100
# Выведи все числа от `1` до `100`.
# Но:
# * числа, делящиеся на `3` → `Fizz`
# * числа, делящиеся на `5` → `Buzz`
# * делящиеся и на `3`, и на `5` → `FizzBuzz`
# Например:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 15 → FizzBuzz
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#         continue
#     elif i % 5 == 0:
#         print("Buzz")
#         continue
#     elif i % 3 == 0:
#         print("Fizz")
#         continue
#     print(i)
#


# 10. Сумма чисел**
# Пользователь вводит `N`.
# Например:
# Input: 10
# Получить:
# 55
# Потому что:
# 1 + 2 + 3 + ... + 10 = 55
# Используй цикл.
# n = int(input("Input: "))
# res = 0
# for i in range(1, n + 1):
#     res += i
# print(res)

# 11. Таблица умножения
# Пользователь вводит число:
# Input: 7
# Получить:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 10 = 70
# n = int(input("Input: "))
# for i in range(1, 11):
#     print(f"{i} x {n} = {i * n}")


#
# **12. Угадай число**
# Создай программу:
#`python
# secret_number = 42
# Пользователь пытается угадать число.
# Если:
# guess < secret → Too low
# guess > secret → Too high
# guess == secret → Correct!
# Программа должна продолжать спрашивать, пока пользователь не угадает.

# secret_number = 42
# count = 0
# guess = int(input("Enter a number: "))
# while guess != secret_number:
#     if guess < secret_number:
#         print("Your guess is too low")
#         guess = int(input("Enter a number: "))
#         count += 1
#     elif guess > secret_number:
#         print("Your guess is too high")
#         guess = int(input("Enter a number: "))
#         count += 1
# else:
#     print("you guessed right")
#     print("c:",count)

# 13. Lists
# Дан список:
# numbers = [10, 5, 23, 8, 42, 15, 3]
# Нужно получить:
# сумму;
# минимальное число;
# максимальное число;
# количество элементов;
# новый список только с чётными числами.
# Сначала попробуй без sum(), min(), max(), потом можешь сделать второй вариант с ними.

# numbers = [10, 5, 23, 8, 42, 15, 3]
# # #a
# # def sum_a(numbers:list):
# #     res = 0
# #     for n in numbers:
# #         res += n
# #     return res
# #
# # def min_a(numbers:list):
# #     res = numbers[0]
# #     for n in numbers:
# #         if n < res:
# #             res = n
# #     return res
# #
# # def max_a(numbers:list):
# #     res = numbers[0]
# #     for n in numbers:
# #         if n > res:
# #             res = n
# #     return res
# #
# # def len_a(numbers:list):
# #     res = 0
# #     for n in numbers:
# #         res += 1
# #     return res
# #
# # print(numbers)
# # print(sum_a(numbers))
# # print(min_a(numbers))
# # print(max_a(numbers))
# # print(len_a(numbers))
# #
# #
# #
# # # b
# # print(numbers)
# # print(sum(numbers))
# # print(min(numbers))
# # print(max(numbers))
# # print(len(numbers))


# 14. Работа со списком
# Дан:
# users = ["Islam", "Ali", "John", "Anna", "Islam", "Bob"]
# Сделай:
# 1. Удали дубликаты
# 2. Отсортируй пользователей
# 3. Добавь нового пользователя
# 4. Удали "John"
# 5. Выведи пользователей через цикл

# users = ["Islam", "Ali", "John", "Anna", "Islam", "Bob"]
# def remove_duplicates(lst):
#     result = []
#     for item in lst:
#         if item not in result:
#             result.append(item)
#     return result
# print(users)
# print("a: ",remove_duplicates(users))
# print("b: ",list(set(users)))
#
#
# print(":sorted:",sorted(users))
#
# users.append("khaddizha")
# print("add new users: ",users[-1])
#
# users.remove("John")
# # users.pop(2)
# print(users)
#
# for user in users:
#     print(user)
#
# n = len(users)
# while n > 0:
#     print(users[n-1])
#     n = n-1


# 15. Tuple + Set
# Создай:
# coordinates = (42.87, 74.60)
# Выведи:
# Latitude: 42.87
# Longitude: 74.60
# Затем:
# numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
# Получить уникальные числа через set.
# coordinates = (42.87, 74.60)
# print("Latitude:", coordinates[0])
# print("Longitude:", coordinates[1])
# numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
# print(set(numbers))

# 16. Dictionary
# Создай словарь пользователя:
# user = {
#     "name": "Islam",
#     "age": 19,
#     "city": "Bishkek",
#     "skills": ["Python", "Django", "FastAPI"]
# }
# Выведи:
# Name:
# Age:
# City:
# Skills:
# Затем добавь:
# email
# is_active
# И через цикл выведи все пары:
# name → Islam
# age → 19
# ...
# user = {
#     "name": "Islam",
#     "age": 19,
#     "city": "Bishkek",
#     "skills": ["Python", "Django", "FastAPI"]
# }
# for key in user.keys():
#     print(f"{key.title()}:")
#
# user["email"] = "saddajkl@gmail.com"
# user["is_active"] = True
#
# for key, value in user.items():
#     print(f"{key.title()}: {value}")

# 17. Функция калькулятора
# Создай функцию:
# calculate(a, b, operation)
# Она должна поддерживать:
# +
# -
# *
# /
# Например:
# calculate(10, 5, "+")
# # 15
#
# calculate(10, 5, "*")
# # 50
# Обязательно обработай деление на 0

# def calculate(a,b,operation):
#     if operation == "+":
#         return a+b
#     elif operation == "-":
#         return a-b
#     elif operation == "*":
#         return a*b
#     elif operation == "/":
#         try:
#             return a/b
#         except ZeroDivisionError:
#             return 0
#     else:
#         return "Invalid operation"
#
# print(calculate(1,2,"+"))
# print(calculate(1,2,"-"))
# print(calculate(1,2,"*"))
# print(calculate(1,2,"/"))


# 18. Функция анализа списка
# Создай:
# analyze_numbers(numbers)
# Она должна вернуть информацию:
# {
#     "min": ...,
#     "max": ...,
#     "sum": ...,
#     "average": ...,
#     "even_count": ...,
#     "odd_count": ...
# }
# Например:
# analyze_numbers([1, 2, 3, 4, 5])

# def analyze_numbers(numbers):
#     res = {
#         "min": min(numbers) if numbers else 0,
#         "max": max(numbers) if numbers else 0,
#         "sum": sum(numbers) if numbers else 0,
#         "average": len(numbers) / sum(numbers) if numbers else 0,
#         "even_count": sum(1 for x in numbers if x % 2 == 0),
#         "odd_count": sum(1 for x in numbers if x % 2 == 1)
#     }
#     return res
# print(analyze_numbers([1, 2, 3, 4, 5]))


# 19. Безопасный ввод
# Создай программу, которая просит:
# Enter your age:
# Если пользователь пишет:
# 19
# → программа работает.
# Если:
# abc
# → программа не падает, а пишет:
# Please enter a valid number.
# Используй try / except.
# Дополнительно добавь проверку, что возраст находится в диапазоне 0–120.

# def get_user_age() -> int:
#   while True:
#     user_input: str = input("Enter your age: ")
#     try:
#       age: int = int(user_input)
#
#       if 0 <= age <= 120:
#         return age
#       else:
#         print("Age must be between 0 and 120.")
#
#     except ValueError:
#       print("Please enter a valid number.")
#
# age: int = get_user_age()
# print(f"Your age is {age}.")

# 20. 🚀 Финальная задача — Mini Bank
# Напиши маленькую банковскую систему.
# Начальный баланс:
# balance = 1000
# Меню:
# 1. Check balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# Программа работает в цикле.
# Requirements:
# Check balance
# Your balance: 1000
# Deposit
# Пользователь вводит сумму:
# Enter amount: 500
# Баланс:
# 1500
# Withdraw
# Если денег достаточно:
# Withdraw successful
# Если недостаточно:
# Insufficient funds
# Нельзя внести отрицательную сумму.
# Нельзя снять отрицательную сумму.
# Неправильный ввод не должен ломать программу.
# И желательно использоват
# def show_balance(...):
# def deposit(...):
# def withdraw(...):
# И type hints, например:
#
# def deposit(balance: float, amount: float) -> float:
#     ...
balance = 1000
active = True

def show_balance():
    return balance

def deposit(balance:float, amount:float) -> float:
    balance += amount
    return balance

def withdraw(balance:float, amount:float) -> float:
    balance -= amount
    return balance

while active:
    print("""
Меню:
1. Check balance
2. Deposit
3. Withdraw
4. Exit
    """)
    enter_operation = input("Enter your choice: ")
    if enter_operation == "1":
        print("Your balance is: ", show_balance())
    elif enter_operation == "2":
        try:
            amount = float(input("Enter your amount: "))
            balance= deposit(balance, amount)
            print("Your balance is: ", show_balance())
        except ValueError:
            print("Please enter a number")
    elif enter_operation == "3":
        try:
            amount = float(input("Enter your amount: "))
            if balance < amount:
                print("Insufficient funds")
            else:
                balance= withdraw(balance, amount)
                print("Your balance is: ", show_balance())
        except ValueError:
            print("Please enter a number")
    elif enter_operation == "4":
        active = False
        print("Thank you for using this application")
    else:
        print("Please enter a valid choice")