
# Функция скачивания изображений

import random
import urllib.request
names = []

def download_img(url):
    name = random.randrange(1, 100)
    name = str(name) + "2" + ".jpg"
    urllib.request.urlretrieve(url, name)


download_img("https://i.ndtvimg.com/i/2017-12/python-istock_650x400_81512639595.jpg")

# 1 Проверка на неповторимость имен
# 2 При ошибке с адресом картинки брать новую или останавливать программу (try except)
# https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
main.py

main.py. На экране.