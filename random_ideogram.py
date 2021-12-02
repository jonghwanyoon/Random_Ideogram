import plotly.graph_objects as go
import random

def random_ideogram():
    fig = go.Figure()
    num_bar = 40
    x = []
    y = []
    for bar_idx in range(num_bar):
        for _ in range(50):
            x.append(bar_idx)
            y.append(random.random())

    fig.add_trace(go.Bar(x=x, y=y, marker={"color":y, "colorscale":"Blues", "line":{"width":0}}))
    fig.update_layout(paper_bgcolor="rgb(255,255,255,1)")
    fig.update_xaxes(showgrid=False, visible=False)
    fig.update_yaxes(showgrid=False, visible=False)
    fig.layout.plot_bgcolor="#000"
    fig.layout.paper_bgcolor="#000"
    return fig


fig = random_ideogram()
fig.write_image("Test.png")