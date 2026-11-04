age = int(input("Сколько вам лет? "))
student = input("Вы студент? (да/нет)")


if age < 18 or student == "да":
    print("Скидка 200 рублей")
else: 
    print("Билет 350 рублей")