from util import BASE_PATH_GOOGLE, HEADERS_GOOGLE
from bs4 import BeautifulSoup
import requests
def search_scholar(wd, page):
    session = requests.Session()
    serach_url = BASE_PATH_GOOGLE+"&q={}&start={}".format(wd, str((int(page)-1)*10))
    req = session.get(serach_url, headers=HEADERS_GOOGLE)
    print(req.text)

if __name__ == '__main__':
    search_scholar("image",1)
