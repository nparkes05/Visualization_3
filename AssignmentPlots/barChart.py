import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

filtered_df = df.head(20)

data = [go.Bar(x=filtered_df['NOC'], y=filtered_df['Total'])]

layout = go.Layout(title='Total medals of the top 20 countries', xaxis_title="Countries",
                   yaxis_title='Number of medals')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='top20Countries.html')
