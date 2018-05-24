import os
import pandas as pd

data_dir = os.path.join(os.getcwd(), "data")
filename = os.path.join(data_dir, "INDU-2007-2014.csv")

if __name__ == "__main__":
    df = pd.read_csv(filename)
    year_ranges = ([
        (0, 3),                 # 2007
        (3, 10),                # 2009
        (10,19),                # 2011
        (19, 42),               # 2013
        (42, len(df.columns))]) # 2014

    years = [2007, 2009, 2011, 2013, 2014]

    for year, (start, end) in zip(years, year_ranges):
        columns = ["instance"] + list(df.columns[start+1:end+1])
        new_df = df[columns]
        df[columns].to_csv(os.path.join(data_dir, "INDU-" + str(year) + ".csv"), index=False)