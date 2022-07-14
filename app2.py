######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
labels = ['Winchester', 'McLarens', 'Moes tavern', 'The drunken clam']
values = [25, 52, 15, 7]
########### Set up the chart

def make_that_cool_piechart(labels, values):
    bar_fig = go.Figure()
    bar_fig.add_trace(go.Pie(
        labels=labels,
        values=values))
    bar_fig.update_layout(title='My favorite bars (in terms of visits per year)')    
    return bar_fig


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_piechart(labels, values)
    fig.write_html('docs/piechart.html')
    print('We successfully updated the piechart!')
