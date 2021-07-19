'''
이름, 나이, 주소를 입력받아서 자기 소개하는 프로그램 작성하시오
출력은 안녕하세요, 제 이름은 Tom이고, 나이는 28세이고 , 서울에서 거주합니다. 로 됩니다
이때, 여러 사람이면 전부 입력 받아서 전체가 일관 출력되는 시스템이어야 합니다
'''

class Person(object):

    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress
        self.scores = []

    def information(self, score):
        self.scores.append(score)

    def myself(self):
       print(f'제 이름은 {self.name}이고, 나이는 {self.age}세이고 , {self.adress}에서 거주합니다')

    @staticmethod
    def main():
        count = int(input('How many ?'))
        result = []
        for i in range(count):
            person = Person(input('name: '), input('age: '), input('adress: '))
            result.append(person)
        for person in result:
           person.myself()

Person.main()