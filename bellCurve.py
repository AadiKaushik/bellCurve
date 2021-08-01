import csv 
import pandas as pd
import plotly.figure_factory as ff


df = pd.read_csv('C:/Users/aadi_/Desktop/coding/python/dataVisulation/data4.csv')

fig = ff.create_distplot([df['Avg Rating'].tolist()],['phonesRating'],show_hist=True)

fig.show()