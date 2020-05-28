# Databricks notebook source
# MAGIC %sh pip install koalas

# COMMAND ----------

import pandas as pd
import numpy as np
import databricks.koalas as ks
import matplotlib.style as style
style.use('seaborn-whitegrid')

# COMMAND ----------

df = ks.read_csv('dbfs:/tmp/wine_data.csv')

# COMMAND ----------

df.info()

# COMMAND ----------

df.columns

# COMMAND ----------

df[['quality', 'vintage']].astype('int', inplace=True)

# COMMAND ----------

df.value_counts()

# COMMAND ----------

df.dtypes

# COMMAND ----------

print("This is a new change!")

# COMMAND ----------
df.columns