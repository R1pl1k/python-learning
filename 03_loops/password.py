password: str = ""
count: int = 0

while password != "1234" and count<=2:
    password = input("Введите пароль: ")
    count += 1

if password == "1234":
    print(f"Доступ разрешён. Попыток: {count}")
else:
    print("Доступ заблокирован")