import csv
import os
import pandas as pd


data_dir = os.path.join(os.getcwd(), "data")
filename = os.path.join(data_dir, "INDU-2007-2014.csv")
csv_filename = os.path.join(data_dir, "SAT_Performance.csv")


def print_avg_score_each_year(df):
    year_ranges = ([
        (2007, 0, 3),                 # 2007
        (2009, 3, 10),                # 2009
        (2011, 10, 19),                # 2011
        (2013, 19, 42),               # 2013
        (2014, 42, len(df.columns))])  # 2014

    results = []
    for year, start, end in year_ranges:
        columns = df.columns[start:end]
        mean_for_each_solver = df[columns].mean()
        mean_for_all_solvers = mean_for_each_solver.mean()
        results.append((year, mean_for_all_solvers))
        # print(mean_for_all_solvers)
    return results


def print_best_score_each_year(df):
    year_ranges = ([
        (2007, 0, 3),                 # 2007
        (2009, 3, 10),                # 2009
        (2011, 10, 19),                # 2011
        (2013, 19, 42),               # 2013
        (2014, 42, len(df.columns))])  # 2014

    results = []
    for year, start, end in year_ranges:
        columns = df.columns[start:end]
        mean_for_each_solver = df[columns].mean()
        max_for_all_solvers = mean_for_each_solver.max()
        results.append((year, max_for_all_solvers))
        # print(mean_for_all_solvers)

    return results


def create_SAT_perf_csv(csv_filename, average_data, best_data):
    with open(csv_filename, 'w') as csvfile:
        sat_writer = csv.writer(csvfile, delimiter=',')
        sat_writer.writerow(["Year", "Average", "Best"])
        for ((year, average), (_, best)) in zip(average_data, best_data):
            sat_writer.writerow([year, average, best])


if __name__ == "__main__":
    df = pd.read_csv(filename)

    def problem_solved(value):
        result, _, _, _, _ = value.split(":")
        return 0.0 if result == "TIMEOUT" else 1.0

    df = df[df.columns[1:]].applymap(problem_solved)
    average_data = print_avg_score_each_year(df)
    best_data = print_best_score_each_year(df)

    create_SAT_perf_csv(csv_filename, average_data, best_data)
