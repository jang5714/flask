from bs4 import BeautifulSoup
import requests
import pandas as pd
from oop import contacts

class Music(object):
    domain =''
    html = ''
    query_string =''
    headers = {'User-Agent':'Mozilla/5.0'}
    tag_name = ''
    fname = ''
    class_name = []
    artists = []
    titles = []
    dict = {}
    df = None

    def set_html(self,):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text

    def get_raking(self):
        soup = BeautifulSoup((self.html), 'lxml')
        a = soup.find_all(name=self.tag_name, attrs={'class': self.class_name[0]})
        t = soup.find_all(name=self.tag_name, attrs={'class': self.class_name[1]})
        for i, j in zip(a, t):
            print("\tArtisis :" + i.find('a').text + " \tTitle :" + j.find('a').text)
            self.artists.append( i.find('a').text)
            self.titles.append( j.find('a').text)

    def insert_dict(self):
        # 방법 1
        #for i in range(0, len(self.tag_name)):
            #self.dict[self.titles[i]] = self.artists[i]
        # 방법 2
        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j
        #방법 3
        #for i, j in enumerate(self.titles):
            #self.dict[j] = self.artists[i]

        print(self.dict)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = f'./data/{self.fname}.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN',encoding='utf-8-sig')



def main():
    mr = Music()
    while 1:
        menu =contacts.menu(['exit','bug (URL),Melon (URL)','output','print dict','dict to dataframe','df to csv'])
        if menu == 0:
            break
        elif menu == 1:
            site = int(input('1-벅스 2-멜론'))
            if site == 1:
                mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
                mr.query_string = 'chartdate=20210720&charthour=16'
                mr.class_name.append('artist')
                mr.class_name.append('title')
                mr.tag_name = 'p'
                mr.set_html()
            else:
                mr.domain = 'https://www.melon.com/chart/index.htm?'
                mr.query_string = 'dayTime=2021072107'
                mr.class_name.append('ellipsis rank02')
                mr.class_name.append('ellipsis rank01')
                mr.tag_name = 'div'
                mr.set_html()
        elif menu == 2:
                mr.get_raking()
        elif menu == 3:
            mr.insert_dict()
        elif menu == 4:
            mr.dict_to_dataframe()
        elif menu == 5:
            mr.fname = 'text'
            mr.df_to_csv()





if __name__ == '__main__':
    main()