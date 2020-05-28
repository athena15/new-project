# Databricks notebook source
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_data(df):
    cols = df["quality", "vintage"]
    df['quality_2'] = int(df['quality'] ** 2)
    return df

# COMMAND ----------

print("Here's a change")