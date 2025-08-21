import pandas as pd
from fetcher import DAL_atlas_mongo
from processor import Processor
import type_conversion as con_type


class Manager:

    def __init__(self, user, password, database, collection):
        self.DAL = DAL_atlas_mongo(user, password, database, collection)
        self.processor = None
        self.data = None


    def fetch_data(self):
        if self.DAL:
            connect = self.DAL.open_connection()
            if connect:
                self.data = self.DAL.get_all()
                self.DAL.close_connection()
            return connect



    def run_processes(self, text_key: str, weapons: list):
        if self.data is not None:
            self.data = con_type.convert_to_df(self.data)
            try:
                self.processor = Processor(self.data, text_key)
                self.processor.add_rarest_words()
                self.processor.add_sentiment()
                self.processor.add_weapons_detected(weapons)
            except:
                return {"Error: the processes not working"}



    def get_processed_data(self):
        if isinstance(self.data, pd.DataFrame):
            json_processed_data = con_type.convert_df_to_json(self.data)
            return json_processed_data

