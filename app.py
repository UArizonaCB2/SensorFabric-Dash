import dash
from dash import html
from dash import dcc 
import plotly.graph_objects as go
import plotly.express as px
from dash import Input, Output, State
import numpy as np

# Sensor Fabric dependencies
# Git - https://github.com/nextgensh/sensorfabric.git
from sensorfabric.ua.sensors import DataSet
from sensorfabric.ua.sensors import Raw

app = dash.Dash()

def hr_graph(time, heart_rate):
    fig = go.Figure([go.Scatter(x=time, y=heart_rate,\
            line=dict(color='firebrick', width=4), name='Heart Rate')
        ])

    fig.update_layout(title = 'Full day fitbit heart rate information',
            xaxis_title='Time (Hours)',
            yaxis_title='Heart Rate (Bpm)'
            )

    return fig


app.layout = html.Div([
    html.Div([
        html.Center([
            html.H1("Demo : Sensor Fabric Demo with MyDataHelps."),
        ])
        ], style={'background-color':'#AB0520', 'margin':0, 'color':'white','font-weight':'bold', 'padding':10}),
    html.Div([
        "Participant ID : ", 
        dcc.Input(id='txt-id', value='MDH-XXXX-XXXX'),
        html.Button('Get Fitbit HR', id='btn-submit', style={'margin-left':10}, n_clicks=0) 
        ], style={'margin-top':40, 'padding':20}),
    html.Br(),
    html.Div(id='hr-output', style={'padding':20, 'background-color':'#ECEFF1'})
])

@app.callback(
    Output('hr-output', 'children'),
    Input('btn-submit', 'n_clicks'),
    State('txt-id', 'value')
)
def update_output(n_clicks, value):
    if n_clicks <= 0:
        return html.Div(['Enter participant ID to fetch data from sensor fabric'])

    # Load the data from the sensor fabric.
    json_buffer = DataSet.load_data('cb2', 'fitbit', '20220620-20220621/fitbit_intraday_activities_heart/'+value+'/activities_heart_date_2022-06-19_1d_1sec.json', env={'DATA_BASE_DIR':'./DataSet/'})
    if json_buffer is None:
        return html.Div(['Could not find participant {}'.format(value)])

    (ret, hr) = Raw.execQuery(json_buffer[0], "SELECT value FROM activities-heart-intraday.dataset")
    if not ret:
        return html.Div(['Could not find data'])

    (ret, time) = Raw.execQuery(json_buffer[0], "SELECT time FROM activities-heart-intraday.dataset")
    if not ret:
        return html.Div(['Could not find data'])

    # We have the data.
    return html.Div([
        dcc.Graph(figure=hr_graph(time, hr)),
        dcc.Markdown(
        """
        ## This was generated using the following sensor fabric code
        ```python
        # Sensor Fabric dependencies
        from sensorfabric.ua.sensors import DataSet
        from sensorfabric.ua.sensors import Raw

        # Load the data from the namespace 'cb2' and sensor type 'fitbit' with the data modality 'intraday_activities_heart' for the participant ID
        value = 'MDH-XXXX-XXXX'
        json_buffer = DataSet.load_data('cb2', 'fitbit', 'intraday_activities_heart/'+value')
        
        # Run Sensor Fabric queries ( A simple SQL like query language that is storage agnostic )
        (ret, hr) = Raw.execQuery(json_buffer[0], "SELECT value FROM activities-heart-intraday.dataset")
        (ret, time) = Raw.execQuery(json_buffer[0], "SELECT time FROM activities-heart-intraday.dataset")

        # hr and time are numpy arrays returned by the fabric layer and can used for analysis.
        ```

        """
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
