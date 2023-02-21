path = "quest.json"
path_url = "https://www.jsonkeeper.com/b/CPTY"
from util import load_json, load_request_json
from quest_class import Question, Plauer

print('Введите имя игрока:', end=' ')
name = input()
#quiestion = load_json(path)
quiestion = load_request_json(path_url)
print(f"Привет {name} начнем игру!")
print(f"{name} составь из слова >>>>{quiestion.word}<<<< {len(quiestion.subword)} слов!")
print("Слова должны быть не короче 3 букв")
print("Для выхода из игры угадайте все слова")
print("или введите слово стоп")
plauer = Plauer(name)
flag = True
while flag:
    user_input = input()
    if len(user_input)<3:
        print("Слишком короткое слово попробуйте еще!!!")
        continue
    if user_input == 'стоп' or user_input =='stop':
        break
    if quiestion.in_correct(user_input):
        if plauer.correct_word(user_input):
            plauer.add_word(user_input)
            print(f"Правильно {plauer.counts_word_plauer()} из {quiestion.counts_word()}")
            if plauer.counts_word_plauer() == quiestion.counts_word():
                flag = False
                break
        else:
            print("Это слово вы уже использовали")
    else:
        print("Неправильное слово либо некорректный ввод!!!")
        print(f"Напомню нужное слово {quiestion.word}")
print(f"Вы угадали {plauer.counts_word_plauer()} из {quiestion.counts_word()} возможных слов")



