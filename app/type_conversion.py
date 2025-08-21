import pandas as pd


def convert_to_df(data):
    df = pd.DataFrame(data)
    return df

def convert_df_to_json(df):
    json = df.to_json(orient="records")
    return json