from modu.template.basic_plot import plot_show, plot_two_list_show, scatter
from common.menu import menu
from modu.template.changedtemperature_my_birthday import ChangedTemperature_My_Birthday

if __name__ == '__main__':
    while 1:
        menu = menu(
            ['exit', 'plot_show', 'plot_two_list_show', 'Scatter', 'Blank','ChangedTemperature_My_Birthday'])

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
        elif menu == 4:
            pass
        elif menu == 5:
            ChangedTemperature_My_Birthday().processing()