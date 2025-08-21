import pandas as pd
from fetcher import DAL_atlas_mongo
from processor import Processor


class Manager:

    def __init__(self, user, password, database, collection):
        self.DAL = DAL_atlas_mongo(user, password, database, collection)
        self.processor = None
        self.data = None
        self.df = None


    def fetch_data(self):
        if self.DAL:
            self.DAL.open_connection()
            self.data = self.DAL.get_all()
            self.DAL.close_connection()


    def convert_data_to_df(self):
        if self.data:
            self.df = pd.DataFrame(self.data)


    def run_processes(self, text_key: str, weapons: list):
        if self.df:
            self.processor = Processor(self.df, text_key)
            self.processor.add_rarest_word()
            self.processor.add_sentiment()
            self.processor.add_weapons_detected(weapons)


    def get_processed_data(self):
        return self.df

