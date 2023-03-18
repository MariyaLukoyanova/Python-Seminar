# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
df = pd.read_csv("california_housing_train.csv")

df.columns

df.loc[(df["population"] < 500) & (df["population"] > 0), "median_house_value"].mean()

df.loc[df["population"] == df["population"].min(), "households"].max()

