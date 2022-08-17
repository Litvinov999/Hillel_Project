# enemy_name = input("Напишите ваше имя: ")
#
# enemy_age = input("Укажите ваш возраст: ")
#
# if not enemy_age.isdigit() or int(enemy_age) <= 0:
#     print("Ошибка повторите ввод")
#
# elif int(enemy_age) < 10:
#     print("Привет, шкет", enemy_name)
#
# elif 10 <= int(enemy_age) <= 18:
#     print("Как жизнь", enemy_name)
#
# elif int(enemy_age) < 100:
#     print("Что желаете", enemy_name)
#
# else:
#     print(enemy_name, ", вы лжёте - в наше время столько не живут...")

enemy_name = input("Напишите ваше имя: ")

enemy_age = input("Укажите ваш возраст: ")


while True:

    if not enemy_age.isdigit() or int(enemy_age) <= 0:
        print("Ошибка повторите ввод")
        ask = input("Желаете выйти?(Д/Y)").split()
        if "Y" in ask or "Д" in ask or "y" in ask or "д" in ask:
            break


    elif int(enemy_age) < 10:
        print("Привет, шкет", enemy_name)
        ask = input("Желаете выйти?(Д/Y)").split()
        if "Y" in ask or "Д" in ask or "y" in ask or "д" in ask:
            break


    elif 10 <= int(enemy_age) <= 18:
        print("Как жизнь", enemy_name)
        ask = input("Желаете выйти?(Д/Y)").split()
        if "Y" in ask or "Д" in ask or "y" in ask or "д" in ask:
            break


    elif int(enemy_age) < 100:
        print("Что желаете", enemy_name)
        ask = input("Желаете выйти?(Д/Y)").split()
        if "Y" in ask or "Д" in ask or "y" in ask or "д" in ask:
            break


    else:
        print(enemy_name, ", вы лжёте - в наше время столько не живут...")
        ask = input("Желаете выйти?(Д/Y)").split()
        if "Y" in ask or "Д" in ask or "y" in ask or "д" in ask:
            break
