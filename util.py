import json
from random import randint
from quest_class import Question


def load_json(path):
    with open(path, "r") as file:
        data_json = file.read()
    words = json.loads(data_json)
    list_word = (words[randint(0, len(words) - 1)])
    return Question(list_word['word'], list_word['subword'])
