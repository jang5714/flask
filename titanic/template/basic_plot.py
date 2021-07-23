import matplotlib.pyplot as plt
from common.menu import menu

'''
list 값은 y축이고, x축은 0부터 1까지 자동으로 증가한다.
'''
def plot_show():
    plt.title('plotting')
    plt.plot([10, 20, 30, 40])
    plt.show()
'''
첫번째 list가 x축이고, 두번째 list가 y축이다.
'''
def plot_two_list_show():
    plt.title('plotting')
    plt.plot([1,3,3,4], label='asc', color='blue', linestyle='--')
    plt.plot([12, 43, 25, 15],label ='bid', color='r', ls=':')
    plt.legend()
    plt.show()

def plot_marker():
    plt.title('marker')
    plt.plot([10, 20, 30, 40], 'r.', label ='circle')
    plt.plot([10, 30, 20, 10], 'g^', label='triangle up')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    while 1:
        menu = menu(
            ['exit', 'plot_show', 'plot_two_list_show', 'plot_marker', 'dict to dataframe', 'df to csv'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
            break
        elif menu == 2:
            plot_two_list_show()
            break
        elif menu == 3:
            plot_marker()
            break