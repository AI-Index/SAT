import pandas as pd

def calculate_average_frechette(df):
    c = float(5000)
    X = float(len(df))
    A = float(len(df.columns)) - 1

    counter = [0]

    def frechette_et_al(value):
        result, t, _, _, _ = value.split(":")
        if result == "TIMEOUT":
            counter[0] += 1
            return 0.0
        t = float(t)
        return 1 + (c - t) / (X * c * A + 1)

    score_conversion = frechette_et_al

    df = df[df.columns[1:]].applymap(score_conversion)
    mean_for_each_solver = df.mean()
    mean_for_all_solvers = mean_for_each_solver.mean()
    print("%.10f" % mean_for_all_solvers, counter[0] / A / X)

if __name__ == "__main__":
    for name in ["INDU-%d.csv" % d for d in [2007, 2009, 2011, 2013, 2014]]:
        df = pd.read_csv(name)
        calculate_average_frechette(df)
