# %%
import pandas as pd
import numpy as np
import plotly.express as px

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

fig = px.histogram(mat, x="sex", color="school")
fig.show()
# Alt
mat.sex.value_counts().sort_values().plot(kind = 'barh')

# %%
# Need to organize the Plots so all print
fig = px.histogram(mat, x="sex", color="reason")
fig.show()

fig = px.histogram(mat, x="sex", color="internet")
fig.show()

fig = px.histogram(mat, x="school", color="internet")
fig.show()

fig = px.histogram(mat, x="sex", color="activities")
fig.show()

fig = px.histogram(mat, x="sex", color="freetime")
fig.show()