import csv
import pandas as pd
import matplotlib.pyplot as plt

'''
next()는 두가지 포맷으로 사용된다.
function 구조로 사용되면 header만 리턴한다.
consumer 구조로 사용되면 data에서 header를 제거한다.

row[날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃)] 최고기온은 -1 이다.


'''
class ChangedTemperature_My_Birthday():
    data: [] = list()
    highest_temperature: [] = list()

    def processing(self):
        self.read_data()
        self.save_data_to_list()
        self.visualize_data()
        self.extract_date_data()

    def read_data(self):
        data = csv.reader(open('./data/unit_5.csv','rt', encoding ='UTF-8'))
        next(data)
        # print([i for i in data])
        self.data = data

    def save_highest_temperatures(self):
        #print([i[-1] for i in self.data])
        return [i[-1] for i in self.data]

    def save_data_to_list(self):
        self.highest_temperature.append([float(i[-1]) for i in self.data if i[-1] != ''])
        print(self.highest_temperature)

    def visualize_data(self):
        pass

    def extract_date_data(self):
        pass


if __name__ == '__main__':
    this = ChangedTemperature_My_Birthday()
    this.read_data()
    #this.save_data_to_list()
    this.save_data_to_list()