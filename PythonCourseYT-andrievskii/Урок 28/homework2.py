from collections import Counter

text = "text.txt"

word_list = []
with open(text, 'r', encoding="utf-8") as F: #Читать c текст
    read_text = F.read()

for word in read_text.split():
   clear_word = ""
   for letter in word:
       if letter.isalpha():
           clear_word += letter.lower()

   word_list.append(clear_word)

print(Counter(word_list))