class Question():
    def __init__(self, word, subword):
        self.word = word
        self.subword = subword
        self.open_word = list()

    def __repr__(self):
        return f'Класс для {self.word}'

    def in_correct(self, user_input):
        self.user_input= user_input
        if self.user_input in  self.subword and self.user_input not in self.open_word:
            print('Правильно')
            self.open_word.append(self.user_input)
            if len(self.subword) == len(self.open_word):
                return False
            else:
                return True
        elif len(self.user_input)<3:
            print('Слишком короткое слово!')
            return True
        elif self.user_input in self.open_word:
            print('Это слово уже было')
            return True
        elif self.user_input == 'stop' or self.user_input == 'стоп':
            print("Завершаем игру")
            return False
        else:
            print('Неправильный ввод или неверное слово')
            return True