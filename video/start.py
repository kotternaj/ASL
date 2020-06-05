
asl_url = 'https://www.signingsavvy.com/search/'

user_input = input("Type words here: ")

split_words = user_input.split(' ')

for word in split_words:
    url_list = []
    url_list.append(asl_url + word)

    print(url_list)
    for item in url_list:
        with 
