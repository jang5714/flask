import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Population_structure_visualization(object):
    data: [] = list()
    name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')

    def read_data(self):
        data = pd.read_csv('data/202106_202106_연령별인구현황_월간.csv', 'rt', encoding='UTF-8', thousands=',')
        #print([i for i in data])
        self.data = data

    def pop_per_dong(self, arr: []):
        for i in self.data:
            if self.name in i[0]:
                arr = np.array(i[3:], dtype=int) / int(i[2])
        return arr

    def pop_per_dong2(self, hom: []):
        for j in self.data:
            if self.name in j[0]:
                hom = np.array(j[3:],dtype=int) / int(j[2])
        return hom

    def show_plot(self, arr: [], hom: []):
        plt.rc('font', family='Malgun Gothic')
        plt.title(self.name + ' 지역의 인구 구조')
        plt.plot(arr)
        plt.plot(hom)
        plt.show()


if __name__ == '__main__':
    pop = Population_structure_visualization()
    pop.read_data()
    pop.show_plot(pop.pop_per_dong(),pop.pop_per_dong2())
