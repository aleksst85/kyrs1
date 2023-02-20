path = "quest.json"
from util import load_json
from quest_class import Question

print('Введите имя игрока:', end=' ')
name = input()
quiestion = load_json(path)
print(f"Привет {name} начнем игру!")
print(f"{name} составь из слова >>>>{quiestion.word}<<<< {len(quiestion.subword)} слов!")
print("Слова должны быть не короче 3 букв")
print("Для выхода из игры угадайте все слова")
print("или введите слово стоп")

while quiestion.in_correct(input()):
    print(end='')
print(f"Вы угадали {len(quiestion.open_word)} из {len(quiestion.subword)} возможных слов")



