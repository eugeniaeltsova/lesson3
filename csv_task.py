dialogue = [
    {"how are you?" : "fine, tnks", "what's your name?" : "jenechka", "where are you from?" : "Russia"},
    {"how are you?" : "ok", "what's your name?" : "leo", "where are you from?" : "Spain"}
]

import csv
with open('get_answer_dict.csv', 'w', encoding='utf-8') as f:
    fields = ['how are you?', 'what\'s your name?', 'where are you from?']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for answer in dialogue:
        writer.writerow(answer)


