answer: str = input("Хотите продолжить? да/нет ")
answer= answer.strip().lower()

if answer == "да":
    print("Продолжаем")
elif answer == "нет":
    print("Выход")
else:
    print("Не понял ответа")