from dash.exceptions import PreventUpdate

def test_callback(values, n_clicks):
    print(values)
    values.test = "TEST"
    raise PreventUpdate