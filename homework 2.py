print("Здравствуй, Евгений, я хочу сыграть с тобой в игру.")

signs = input("Напиши самое длинное слово которое знаешь: ")

even_signs = signs[1::2]

reverse_signs_big = signs[-1::-1]

print(signs)
print(even_signs)
print(reverse_signs_big.upper())
