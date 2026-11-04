password: str = ""
count: int = 0

while password != "1234" and count<=2:     # ← второе условие про count
    password = input("Введите пароль: ")
    count += 1

if password == "1234":                               # ← почему закончился цикл?
    print(f"Доступ разрешён. Попыток: {count}")
else:
    print("Доступ заблокирован")