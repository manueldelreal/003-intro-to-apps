######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
pies=['Cheesecake', 'Peach Cobbler', 'Apple', 'Pinneaple']
deliciousness=[100, 60, 85, 75]
crunchyness=[10, 25,42, 55]
color1='seagreen'
color2='turquoise'
mytitle='My favorite pies (in terms of deliciousness and crunchyness)'

label1='Delicious'
label2='Crunchy'

########### Set up the chart

def make_that_cool_barchart(pies, deliciousness, crunchyness, color1, color2, mytitle):
    delicious = go.Bar(
        x=pies,
        y=deliciousness,
        name=label1,
        marker={'color':color1}
    )
    crunchy = go.Bar(
        x=pies,
        y=crunchyness,
        name=label2,
        marker={'color':color2}
    )

    pie_data = [delicious, crunchy]
    pie_layout = go.Layout(
        barmode='group',
        title = mytitle
    )

    pie_fig = go.Figure(data=pie_data, layout=pie_layout)
    return pie_fig


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_barchart(pies, deliciousness, crunchyness, color1, color2, mytitle)
    fig.write_html('docs/barchart.html')
    print('We successfully updated the barchart!')