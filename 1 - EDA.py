# Databricks notebook source
# MAGIC %sh pip install koalas

# COMMAND ----------

import pandas as pd
import numpy as np
import databricks.koalas as ks

# COMMAND ----------

x = 5
print(x)

# COMMAND ----------

y = 10
z = 20
print(y+z)

# COMMAND ----------

a = 2
b = 3
c = 5
d = 10

# COMMAND ----------

print('This is a change!')
print('This is another change!')
print("And finally, a third change!")

# COMMAND ----------

def squared(x):
  return x **2
