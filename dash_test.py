import dash
app = dash.Dash()
app.layout = dash.html.Div("hello world")
app.run_server(debug=True)