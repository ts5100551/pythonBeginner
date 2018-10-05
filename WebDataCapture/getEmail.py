import requests, re
regex = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
url = 'https://www.cyut.edu.tw/~ckhung/c/ai189/'
html = requests.get(url)
emails = regex.findall(html.text)
for email in emails:
    print(email)