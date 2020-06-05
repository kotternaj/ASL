from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

asl_url= 'https://aslteachingresources.com/dictionary/'
words = []

text_input = input("Enter your words: ")

words = text_input.split(' ')

for word in words:
    new_url = asl_url + word
    html = urlopen(new_url)
    res = BS(html.read(), features="html.parser")
    tags = res.findAll("iframe")[1].attrs['src']
    word_string = str(word)
    tag_string = str(tags)
    print("For the word: " +  word_string + " " + "the video is: " + tag_string)
