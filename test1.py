from http import server
import dash
import dash_core_components as dcc
import dash_html_components as html
import gunicorn

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)
server=app.server

app.layout = html.Div(children=[

    html.H1(
        children='Apresentação da biblioteca Dash!',
        style={'textAlign':'center'}
    ),

   html.Div(children='''
        Dash: Aplicação na internet em Python.
    '''),


     dcc.Graph(
        id='example-graph',
        figure={
            'data':[

                 {
                    'x':[0,1,2,3,4,5,6],
                    'y':[0,1,2,3,4,5,6],
                    'type':'line+markers',
                    'name':'Reta'
                },

                {
                    'x':[0,1,2,3,4,5,6],
                    'y':[0,1,4,9,16,25,36],
                    'type':'line+markers',
                    'name':'Parábola'
                }
            ],
            'layout':{'title':'Gráfico (exemplo)'}
        }
    )
    
])

if __name__ == '__main__':
    app.run_server(debug=True)