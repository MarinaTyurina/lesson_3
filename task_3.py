import string
import re

text_lesson = open('story.txt', 'r', encoding='UTF-8')

text_lesson = text_lesson.read()

# 1) методами строк очистить текст от знаков препинания;

text_lesson = text_lesson.replace('.', '')
text_lesson = text_lesson.replace(',', '')
text_lesson = text_lesson.replace('—', '')
text_lesson = text_lesson.replace('?', '')
text_lesson = text_lesson.replace('!', '')
text_lesson = text_lesson.replace('«', '')
text_lesson = text_lesson.replace('»', '')
text_lesson = text_lesson.replace(';', '')

text_lesson = text_lesson.lower()
# 2) сформировать list со словами (split);

text_lesson = text_lesson.split()

# 3) привести все слова к нижнему регистру (map);

print ('Текст в нижнем регистре:', text_lesson)


# 4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;

dict ={}

for word in text_lesson:
    dict[word] = text_lesson.count(word)

dict_2 = list(dict.items())
print('Количество повторений слов:', dict_2)

# 5) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).

# top_5 = dict_2.sort(key=lambda i: i[1], revers = True)
# # top_5 = dict_2[0:5]

top_5 = list(dict.values())
top_5.sort()

for i in range(5):
    top_6 = int(len(top_5))-1-i
    top_7 = top_5[top_6]

    for key, value in dict.items():
        if value == top_7:
            print('Слово в тексте: "', key, '" встречается:', value, 'раз')

word_set = set(text_lesson)
word_quant = (len(word_set))
print('Количество разных слов:', word_quant)

