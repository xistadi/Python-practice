from collections import Counter

text = 'text.txt'
word_list = []
with open(text, encoding='utf-8') as txt:
    txt = txt.read()
for word in txt.split():
    clear_word = ""
    for letter in word:
        if letter.isalpha():
            clear_word += letter.lower()

    word_list.append(clear_word)

print(Counter(word_list))