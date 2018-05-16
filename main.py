import pandas as pd

filename = "INDU-2007-2014.csv"

def print_avg_score_each_year(df):
    year_ranges = ([
        (0, 3),                 # 2007
        (3, 10),                # 2009
        (10,19),                # 2011
        (19, 42),               # 2013
        (42, len(df.columns))]) # 2014

    for start, end in year_ranges:
        columns = df.columns[start:end]
        mean_for_each_solver = df[columns].mean()
        mean_for_all_solvers = mean_for_each_solver.idxmax()
        print(mean_for_all_solvers)

if __name__ == "__main__":
    df = pd.read_csv(filename)
    c = float(5000)
    X = float(len(df))
    A = float(len(df.columns)) - 1

    def frechette_et_al(value):
        result, t, _, _, _ = value.split(":")
        if result == "TIMEOUT":
            return 0.0
        t = float(t)
        return 1.0
        # return 1 + (c - t) / (X * c * A + 1)

    def rev_par_2(value):
        result, t, _, _, _ = value.split(":")
        if result == "TIMEOUT":
            return 0.0
        t = float(t)
        return 1.0
        # return 1 - (t / 10000)

    # score_conversion = frechette_et_al
    score_conversion = rev_par_2
    df = df[df.columns[1:]].applymap(score_conversion)
    print_avg_score_each_year(df)
