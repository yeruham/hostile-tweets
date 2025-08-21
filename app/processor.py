import pandas as pd


class Processor:

    def __init__(self, data_frame: pd.DataFrame, text_column: str):

        if not isinstance(data_frame, pd.DataFrame):
            raise TypeError (f"the {data_frame} must be a DataFrame instance")
        if not text_column in data_frame.columns:
            raise ValueError (f"the {text_column} not in {data_frame}")

        self.df = data_frame
        self.text_column = text_column

    def add_rarest_word(self):
        pass

    def add_sentiment(self):
        pass

    def add_weapons_detected(self, weapons: list):
        pass



