
from bs4 import BeautifulSoup

def get_images(user):

    soup = BeautifulSoup(request.urlopen("https://www.instagram.com/"+str(user)),'lxml')
    for image in soup.findAll('img'):
        href = image.get('src')
        print(href)
get_images('user')



import requests
from bs4 import BeautifulSoup


def get_images(user):
    url = "https://www.instagram.com/" + str(user)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for image in soup.findAll('img'):
        href = image.get('src')
        print(href)

get_images('mansi_sharma12')


