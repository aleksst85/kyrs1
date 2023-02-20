path = "quest.json"
from util import load_json
from quest_class import Question

word, subword = load_json(path)
print("Ваше слово", word)
quiestion = Question(word, subword)

while quiestion.in_correct(input()):
    print(end='')




