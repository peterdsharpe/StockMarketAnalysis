import pandas as pd
import os

sp_500_max = pd.read_csv(
    os.path.abspath("../data/sp_500_max.csv"),
    sep=","
)
