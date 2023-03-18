# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
df = pd.read_csv("california_housing_test.csv")

df.shape

df.dtypes

df.isnull().sum()

# df[df["median_income"]<2]["median_house_value"]
df.loc[df["median_income"]<2, "median_house_value"]

df[["longitude", "latitude"]]

df[(df["housing_median_age"]<20) & (df["median_house_value"]>70000)]

df['median_house_value'].max()

df['median_house_value'].min()

df.loc[df["median_income"] == 3.1250, "median_house_value"].max()

#df[df["median_house_value"] == df["median_house_value"].min()]["population"].max()
df.loc[df["median_house_value"] == df["median_house_value"].min(), "population"].max()

