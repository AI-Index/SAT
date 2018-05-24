**Generating yearly performance CSV**

Takes in a CSV with performance data of SAT Solvers on problems from the SAT Competition from 2007 - 2014. Produces, for each year, the average percentage of problems completed by solvers submitted to the competition that year and the percentage of the solver that solved the most problems from the comptition that year.

Run `python main.py` to generate `data/SAT_Performance.csv`

**Viewing performance for each year**

`python split-csv.py` splits up up the main competition data CSV and splits it up by year for easier viewing. 