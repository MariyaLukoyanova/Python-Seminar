# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()



# Первое решение - для конкретно этого случая
# ниже более универсальное решение :)
null_df = pd.DataFrame(data, columns=["human", "robot"])
dict_1={"human":1, "robot":0}
dict_2={"human":0, "robot":1}
null_df["human"] = data["whoAmI"].map(dict_1)
null_df["robot"] = data["whoAmI"].map(dict_2)
null_df.head()

# Более универсальное решение:)
col = set(data["whoAmI"])
null_or_one=list()
for i in col:
    list0=[]
    for j in data["whoAmI"]:
        if str(j) == i:
            list0.append(1)
        else:
            list0.append(0)
    null_or_one.append(list0)
print(null_or_one)
null_df = pd.DataFrame(null_or_one).transpose()
null_df.columns=col
null_df.head()

# get_dummies для сравнения результата
pd.get_dummies(data['whoAmI'])

