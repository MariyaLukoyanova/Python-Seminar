# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
import seaborn as sns
df = pd.read_csv("california_housing_train.csv")
df.columns

sns.scatterplot(data=df, x="households", y="population")

sns.relplot(x="longitude", y="median_house_value", kind="line", data=df)

sns.histplot(data=df, x="housing_median_age")

sns.histplot(data=df, x="housing_median_age", hue="housing_median_age")

penguins = sns.load_dataset("penguins")
penguins.head()

import seaborn as sns
penguins.columns

sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="sex", size=5)

sns.set(style="darkgrid")
sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="sex")

columns = ["sex", "bill_length_mm", "body_mass_g", "bill_depth_mm"]
g = sns.PairGrid(penguins[columns])
g.map(sns.scatterplot)

sns.histplot(data=penguins, x="body_mass_g")

penguins.loc[penguins["bill_length_mm"]>=42, "bill_size"]="high"
penguins.loc[(penguins["bill_length_mm"]>=35) & (penguins["bill_length_mm"]<42), "bill_size"]="middle"
penguins.loc[penguins["bill_length_mm"]<35, "bill_size"]="low"
penguins.head()

sns.histplot(data=penguins, x="flipper_length_mm", hue="bill_size")

