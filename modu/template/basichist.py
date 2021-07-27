import matplotlib.pyplot as plt
import random

from modu.template import ChangedTemperature_My_Birthday


def hist_show():
    plt.hist([1,1,2,3,4,5,6,6,7,8,10])
    plt.show()

def show_dice(count):
   ls = []
   [ls.append(random.randint(1, 6)) for i in range(count)]
   return ls

def show_hist(ls):
    plt.hist(ls, bins=6)
    plt.show()

def highest_temperature(month: str)-> []:
    birth = ChangedTemperature_My_Birthday()
    birth.read_data()
    aug = []
    [aug.append(float(i[-1])) for i in birth.data if i[-1] != '' if i[0].split('-')[1] == month]
    return aug
    # birth.read_data()
    # jan = []
    # [jan.append(float(i[-1])) for i in birth.data if i[-1] != '' if i[0].split('-')[1] == month01]


def show_hist_about(aug: [], month: str):
    plt.hist(aug, bins=100, color='r', label=f'{month}')
    plt.legend()
    plt.show()



if __name__ == '__main__':
    #ls = show_dice(1000000)
    #show_hist(ls)
    show_hist_about(highest_temperature('05'), month='02')