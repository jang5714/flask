from titanic2.models.dataset2 import Dataset2
from titanic2.models.service import Services


class View (object):
    service = Services()
    data = Dataset2()

    def modeling(self, train, test):
        this = self.prepreessing(train, test)
        print(type(this.train))
        print(this.train.head(2))
        print(this.test.head(2))




    def prepreessing(self, train, test) -> object:
        service = self.service
        this = self.data
        this.train = service.new_models(train)
        this.text = service.new_models(test)
        return this


if __name__ == '__main__':
    view = View
    view.modeling('train.csv','test.csv')