import matplotlib.pyplot as plt
import random

from modu.template import ChangedTemperature_My_Birthday
from modu.template.basichist import highest_temperature

def sorted_random_arr()->[]:
    arr = []
    [arr.append(random.randint(1,1000)) for i in range(13)]
    return arr

def show_boxplot(arr: []):
    plt.boxplot(arr)
    plt.show()

def show_boxplot_month(month: str):
    plt.boxplot(highest_temperature(month))
    plt.show()

def show_boxplot_seven_month():
    birth = ChangedTemperature_My_Birthday()
    birth.read_data()
    arr = birth.data
    month = [[], [], [], [], [], [], [], [], [], [], [], []]
    # for i in arr:
    #     if i[-1] != '':
    #         month[int(i[0].split('-')[1])-1].append(float(i[-1]))
    [month[int(i[0].split('-')[1]) - 1].append(float(i[-1])) for i in arr if i[-1] != '']
    plt.boxplot(month)
    plt.show()

def show_boxplot_all_day(month: str):
    birth = ChangedTemperature_My_Birthday()
    birth.read_data()
    arr = birth.data
    m = []
    [m.append([]) for i in range(31)]
    [m[int(i[0].split('-')[2])-1].append(float(i[-1]))
        for i in arr
            if i[-1] != ''
                if i[0].split('-')[1] == month]

    plt.style.use('ggplot') # Graph Size
    plt.figure(figsize=(10,5), dpi=300) # Graph Size
    plt.boxplot(m, showfliers=False) #Omit Outlier
    plt.show()



def show_boxplot_per_date():
    pass

if __name__ == '__main__':
    #show_boxplot(sorted_random_arr())
    #show_boxplot_month('09')
    #show_boxplot_seven_month()
    show_boxplot_all_day('08')