from bs4 import BeautifulSoup as BS
import urllib.request
import time

def getVidURL(text_input):

    asl_url= 'https://aslteachingresources.com/dictionary/'
    words = []
    url_list = []
    vid_url = []
    vid_dict = {}
    words = text_input.split(' ')
    words = [word.capitalize() for word in words]
    #append each word inputted to the URL of the ASL site
    for word in words:
        url_list.append(asl_url + word)

    #find the iframe URL for each item in the url_list and add to new list
    for url in url_list:
        start_time = time.time()
        with urllib.request.urlopen(url) as response:
            res = BS(response.read(), features="html.parser")
            vid_url.append(res.findAll("iframe")[1].attrs["src"])
            print(vid_url)
            print("--- %s seconds ---" % (time.time() - start_time))
    #combine both lists into a dict with word inputted as key and iframe URL as value
    vid_dict = {words[i]: vid_url[i] for i in range(len(words))}.items()
    print(vid_dict)
    return vid_dict

if __name__ == '__main__':
    getVidURL(input("Enter your words here: "))
