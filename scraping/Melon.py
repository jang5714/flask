from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse



class Melon():
    def __init__(self, url):
        self.url = url
        self.header01 = {'User-Agent':'Mozilla/5.0'}

    def scrap(self):
        x = urllib.request.Request(self.url, headers=self.header01)
        soup = BeautifulSoup(urllib.request.urlopen(x).read(), 'html5lib')
        n_artists = 0
        ls = soup.find_all(name='div', attrs={'class':'ellipsis rank02'})
        ls2 = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        for i, j in zip(ls, ls2):
            n_artists += 1
            print("Rank " + str(n_artists)+"\nArtisis :"+i.find('a').text+" \nTitle :"+j.find('a').text)


def main():
    Melon('https://www.melon.com/chart/index.htm?dayTime=2021072107').scrap()


if __name__ == '__main__':
    main()