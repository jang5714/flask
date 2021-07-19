'''
국어Kor 영어 Eng 수학 Math를  입력받아서
평균점수를 통해  A ~ F학점을 출력하시요
'''

class Grade(object):

    def __init__(self, kor, eng, math,name):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def average(self):
        return self.sum()/3

    @staticmethod
    def main():
            kor = int(input('Korean: \n'))
            eng = int(input('English: \n'))
            math = int(input('Math: \n'))
            grade = Grade(kor, eng, math) #생성자 초기화
            score = grade.average()
            print(grade.average())
            if score >= 90:
                print('A학점 입니다')
            elif score >= 80:
                print('B학점 입니다')
            elif score >= 70:
                print('C학점 입니다')
            elif score >= 60:
                print('D학점 입니다')
            else:
                print('F학점 입니다')

Grade.main()