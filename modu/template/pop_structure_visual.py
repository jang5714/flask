import csv
import matplotlib.pyplot as plt

class Population_structure_visualization(object):
    data: [] = list()


    def read_data(self):
        data = csv.reader(open('data/202106_202106_연령별인구현황_월간.csv', 'rt', encoding='UTF-8'))
        next(data)
        #print([i for i in data])
        self.data = data

    def pop_per_dong(self, dong: str) -> []:
        arr = []
        [arr.append(int(j)) for i in self.data if dong in i[0] for j in i[3:]]
        print(arr)
        return arr

    def show_plot(self, arr: []):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()


if __name__ == '__main__':
    pop = Population_structure_visualization()
    pop.read_data()
    #pop.pop_per_dong('역삼1동')
    pop.show_plot(pop.pop_per_dong('대치1동'))
