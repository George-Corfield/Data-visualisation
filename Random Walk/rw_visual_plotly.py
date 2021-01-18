import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

fig = go.Figure(data= go.Scatter(
    x=rw.x_values,
    y=rw.y_values,
    mode = 'markers',
    name = 'Random Walk',
    marker = dict(color=np.arange(rw.num_points),
                  size = 8,
                  colorscale = 'Blues',
                  showscale = True
                  )
    ))

fig.show()
