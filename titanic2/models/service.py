from titanic2.models.dataset2 import Dataset2
import pandas as pd


class Services():
    data = Dataset2()

    def new_models(self, payload):
        this = self.data
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context,this.fname)