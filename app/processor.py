import pandas as pd


class Processor:

    def __init__(self, data_frame: pd.DataFrame, text_column: str):

        if not isinstance(data_frame, pd.DataFrame):
            raise TypeError (f"the {data_frame} must be a DataFrame instance")
        if not text_column in data_frame.columns:
            raise ValueError (f"the {text_column} not in {data_frame}")

        self.df = data_frame
        self.text_column = text_column



    def add_rarest_words(self):
        text_series = self.df[self.text_column]
        rarest_words = []
        for text in text_series:
            num_by_words = {}
            words = text.split()
            for word in words:
                try:
                    num_by_words[word] += 1
                except:
                    num_by_words[word] = 1

            rarest_word = ""
            num_by_word = len(words) + 1
            for k, v in num_by_words.items():
                if num_by_word == 1:
                    break
                if v < num_by_word:
                    rarest_word = k
                    num_by_word = v

            rarest_words.append(rarest_word)

        self.df.loc[:, 'rarest_word'] = rarest_words




    def add_sentiment(self):
        pass

    def add_weapons_detected(self, weapons: list):
        text_series = self.df[self.text_column]
        weapons_detected = []
        for text in text_series:
            words = text.split()
            weapon_found = False
            for word in words:
                if word in weapons:
                    print(word)
                    weapons_detected.append(word)
                    weapon_found = True
                    break

            if not weapon_found:
                weapons_detected.append("")

        self.df.loc[:, 'weapons_detected'] = weapons_detected




