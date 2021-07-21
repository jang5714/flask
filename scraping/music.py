from bs4 import BeautifulSoup
import requests
import pandas as pd

class Music(object):
    domain=''
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
        menu = int(input('0- exit, 1-bug (URL), 2-Melon (URL)  3-output\n 4-print dict, 5-dict to dataframe, 6-df to csv'))
        if menu == 0:
            break
        elif menu == 1:
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string ='chartdate=20210720&charthour=16'
            mr.set_html()
        elif menu == 2:
            mr.domain = 'https://www.melon.com/chart/index.htm?'
            mr.query_string = 'dayTime=2021072107'
            mr.set_html()
        elif menu == 3:
            mr.class_name.append('ellipsis rank02')
            mr.class_name.append('ellipsis rank01')
            mr.tag_name = 'div'
            mr.get_raking()
        elif menu == 4:
            mr.insert_dict()
        elif menu == 5:
            mr.dict_to_dataframe()
        elif menu == 6:
            mr.fname = '멜론'
            mr.df_to_csv()





if __name__ == '__main__':
    main()