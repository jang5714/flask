from scraping.models.dataset import Dataset
from scraping.models.service import Service

class View (object):
    dataset = Dataset()
    service = Service()

    def modeling(self, bugs, melon):
        modeling = self.proprcessing(bugs, melon)
        print(type(modeling.context))
        print(modeling.context.head(2))
        print(modeling.fname.head(2))

    def proprcessing(self, bugs, melon):
        this = self.dataset
        service = self.service
        this.context = service.new_model(bugs)
        this.fname = service.new_model(melon)
        return this


if __name__ == '__main__':
    view = View()
    view.modeling('bugs.csv','melon.csv')
