class Question:
    def __init__(self, word, subword):
        self.word = word
        self.subword = subword

    def __repr__(self):
        return f'Класс для {self.word}'

    def in_correct(self, user_input):
        self.user_input = user_input
        return self.user_input in self.subword
    def counts_word(self):
        return len(self.subword)
class Plauer:
    def __init__(self, name):
        self.name = name
        self.plauer_word=list()


    def counts_word_plauer(self):
        return len(self.plauer_word)

    def add_word(self, word):
        self.plauer_word.append(word)

    def correct_word(self, word):
        return word not in self.plauer_word
