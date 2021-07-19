class Grade(object):

    def __init__(self, name):
        self.name = name
        self.scores = []

    def addScores(self, score):
        self.scores.append(score)

    def average(self):
        return sum(self.scores) / len(self.scores)

    @staticmethod
    def main():
        grade = Grade(input('name: '))
        for i in ['Korea','English','Math']:
            grade.addScores(int(input(f'{i}: ')))

        name = grade.name
        score = grade.average()
        if score >= 90:
            print(name + 'A학점 입니다')
        elif score >= 80:
            print(name + 'B학점 입니다')
        elif score >= 70:
            print(name + 'C학점 입니다')
        elif score >= 60:
            print(name + 'D학점 입니다')
        else:
            print(grade.name, 'F학점 입니다')


Grade.main()