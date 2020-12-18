import random
import urllib.request
names = []

def download_img(url):
    name = random.randrange(1, 100)
    name = str(name) + "2" + ".jpg"
    urllib.request.urlretrieve(url, name)


download_img("https://i.ndtvimg.com/i/2017-12/python-istock_650x400_81512639595.jpg")
