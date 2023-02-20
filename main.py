path = "quest.json"
from util import load_json
from quest_class import Question

print('Введите имя игрока:', end=' ')
name = input()
print(f"Привет {name} начнем игру!")
print(f"{name} составь из слова {word} {len(subword)} слов!")
print("Слова должны быть не короче 3 букв")
print("Для выхода из игры угадайте все слова")
print("или введите слово стоп")
quiestion = load_json(path)

while quiestion.in_correct(input()):
    print(end='')




