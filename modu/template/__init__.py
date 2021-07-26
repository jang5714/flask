from modu.template.basic_plot import plot_show, plot_two_list_show, scatter
from common.menu import menu

if __name__ == '__main__':
    while 1:
        menu = menu(
            ['exit', 'plot_show', 'plot_two_list_show', 'Scatter', 'df to csv'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
            break
        elif menu == 2:
            plot_two_list_show()
            break
        elif menu == 3:
            scatter()
            break