password = ""
attempts = 0 

while password != 1234 and attempts<3:
    password: int = int (input("Введите пароль: "))
    attempts +=1
if password == 1234:
    print(f"Пароль верный, проходите. Число попыток: {attempts}")
else:
    print("Вход запрещен")

