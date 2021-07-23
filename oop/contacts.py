'''
name, phone, email, address
'''
from common.menu import menu


class PhoneBook():

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


    def to_string(self):
        print(f'\n[InFor]\nname: {self.name} \nphone: {self.phone}\nemail: {self.email}\naddress: {self.address}')


def set_contact() -> object:
    return PhoneBook(input('name'),input('phone'),input('email'),input('address'))


def get_contact(ls):
    for i in ls:
       i.to_string()


def del_contact(ls, name):
    for i, j in enumerate(ls):
       if name == j.name:
           del ls[i]





def main():
    ls =[]
    while 1:
        m = menu(['exit','add','print','delete'])
        if m == 0:
            return
        elif m == 1:
            t = set_contact()
            ls.append(t)
        elif m == 2:
            get_contact(ls)
        elif m == 3:
            del_contact(ls, input('del name'))
        else:
            break




if __name__ == '__main__':
    #ls = ['0-exit', '1-add','2-print','3-delete']
    #ls2 = ['exit','add','print','delete']
    #print(main())
    main()