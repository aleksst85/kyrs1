
import json



with open("quest.json", "r") as file:
    data_json = file.read()
words = json.loads(data_json)
for word in words:
    print(word)
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


