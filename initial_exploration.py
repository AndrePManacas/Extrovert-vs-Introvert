# %%
import pandas as pd
import numpy as np

pd.options.display.max_columns = 999

mat = pd.read_csv("student-mat.csv")
por = pd.read_csv("student-por.csv")

# %%
print("################# Mat #################")
display(mat.head())
print(f"Mat shape: {mat.shape}")
display("Mat Describe", mat.describe())
print(f"Mat info: {mat.info()}")
print("Missing values Count:\n",mat.isnull().sum().sort_values(ascending=False))

print("Duplicate Count")
print(mat[mat.duplicated()].shape)
print(mat.duplicated().sum())

print("################# Por #################")
display(por.head())
print(f"por shape: {por.shape}")
display("por Describe", por.describe())
print(f"por info: {por.info()}")
print("Missing values Count:\n",por.isnull().sum().sort_values(ascending=False))

print("Duplicate Count")
print(por[por.duplicated()].shape)
print(por.duplicated().sum())

# %%
