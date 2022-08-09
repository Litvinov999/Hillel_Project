first_second_name = (input("Напишите Фамилию и Имя: ")).split()

first = (first_second_name[1]).upper()

second = (first_second_name[0]).title()

reverse = f"!{first} <<<>>> {second}?"

create_file = open("homework_4.txt", "w")

print(reverse, file=create_file, end="")

create_file.close()