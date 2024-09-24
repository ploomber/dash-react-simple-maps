from pathlib import Path
import json

import dash_react_simple_maps
from dash import Dash, html, Input, Output, callback_context
from dash_react_simple_maps.constants import ProjectionType, ProjectionConfig, Style

# Tailwind CSS CDN
external_scripts = ["https://cdn.tailwindcss.com"]

app = Dash(__name__, external_scripts=external_scripts)


geoUrl = "https://raw.githubusercontent.com/MinnPost/simple-map-d3/refs/heads/master/example-data/world-population.geo.json"

# this also works
# geoUrl = json.loads(Path("world-population.geo.json").read_text())


map_basic = dash_react_simple_maps.DashReactSimpleMaps(
    id="map-basic",
    geoUrl=geoUrl,
    projection=ProjectionType.GEO_AZIMUTHAL_EQUAL_AREA,
    stroke="#6c757d",
    strokeWidth=1.0,
    fill="#f9f7f3",
)

map_styled = dash_react_simple_maps.DashReactSimpleMaps(
    id="map-styled",
    geoUrl=geoUrl,
    projection=ProjectionType.GEO_AZIMUTHAL_EQUAL_AREA,
    style=Style(
        default={
            "fill": "#fefae0",
            "stroke": "#283618",
            "strokeWidth": 0.5,
        },
        hover={
            "fill": "#dda15e",
            "stroke": "#606c38",
            "strokeWidth": 0.5,
        },
    ),
)

map_annotations = dash_react_simple_maps.DashReactSimpleMaps(
    id="map-annotations",
    annotations=[
        {
            "coordinates": [-100, 40],
            "dx": -30,
            "dy": -30,
            "text": "North America",
            "textColor": "#5BC748",
        },
        {
            "coordinates": [15, 50],
            "dx": 50,
            "dy": -30,
            "text": "Europe",
            "textColor": "#4877C7",
        },
        {
            "coordinates": [20, 0],
            "dx": 30,
            "dy": 30,
            "text": "Africa",
            "textColor": "#C79248",
        },
    ],
    projection=ProjectionType.GEO_AZIMUTHAL_EQUIDISTANT,
    fill="#f9f7f3",
    stroke="#0fa3b1",
    strokeWidth=0.4,
)

map_projection_config = dash_react_simple_maps.DashReactSimpleMaps(
    id="map-projectionconfig",
    geoUrl=geoUrl,
    projection=ProjectionType.GEO_AZIMUTHAL_EQUIDISTANT,
    projectionConfig=ProjectionConfig(
        rotate=[-20, 0, 0],
        center=[10, 10],
        scale=150,
    ),
)

map_markers = dash_react_simple_maps.DashReactSimpleMaps(
    id="map-markers",
    projection=ProjectionType.GEO_MERCATOR,
    geoUrl=geoUrl,
    markers=[
        {
            "markerOffset": -30,
            "name": "Brasilia",
            "coordinates": [-47.8825, -15.7942],
            "markerColor": "#FF5533",
            "textColor": "#FFFFFF",
            "fontSize": "22px",
            "textStrokeColor": "#FF5533",
            "textStrokeWidth": 0.4,
        },
        {
            "markerOffset": -30,
            "name": "Buenos Aires",
            "coordinates": [-58.3816, -34.6037],
        },
        {
            "markerOffset": 15,
            "name": "Bogota",
            "coordinates": [-74.0721, 4.711],
        },
        {
            "markerOffset": -30,
            "name": "Caracas",
            "coordinates": [-66.9036, 10.4806],
        },
        {
            "markerOffset": 15,
            "name": "Lima",
            "coordinates": [-77.0428, -12.0464],
        },
    ],
)

map_lines = dash_react_simple_maps.DashReactSimpleMaps(
    id="map-lines",
    projection=ProjectionType.GEO_MERCATOR,
    lines=[
        {
            "from": [-99.1332, 19.4326],  # Mexico City coordinates
            "to": [-3.7038, 40.4168],  # Madrid coordinates
            "stroke": "#0077b6",
            "strokeWidth": 2,
            "strokeLinecap": "round",
        },
        {
            "from": [-3.7038, 40.4168],  # Madrid coordinates
            "to": [-0.1276, 51.5074],  # London coordinates
            "stroke": "#0077b6",
            "strokeWidth": 2,
            "strokeLinecap": "round",
        },
    ],
    geoUrl=geoUrl,
)


map_colorproperty = dash_react_simple_maps.DashReactSimpleMaps(
    id="map-colorproperty",
    projection=ProjectionType.GEO_MERCATOR,
    geoUrl=geoUrl,
    colorProperty="POP2005",
    colorDomain=[0, 300_000_000],
    colorRange=["#FFF", "#06F"],
)


map_demo = dash_react_simple_maps.DashReactSimpleMaps(
    id="map-demo",
    projection=ProjectionType.GEO_MERCATOR,
    geoUrl=geoUrl,
    colorProperty="POP2005",
    colorDomain=[0, 300_000_000],
    colorRange=["#FFF", "#06F"],
    style={
        "hover": {
            "fill": "#0047B3",
            "stroke": "#E8F1FF",
            "strokeWidth": 0.5,
        }
    },
)


# Define a mapping of map types to their corresponding components
map_types = {
    "demo": map_demo,
    "styled": map_styled,
    "basic": map_basic,
    "annotations": map_annotations,
    "projectionconfig": map_projection_config,
    "markers": map_markers,
    "lines": map_lines,
    "colorproperty": map_colorproperty,
}

DEFAULT_MAP = "demo"

# Create a list of buttons for switching between maps
map_buttons = html.Div(
    [
        html.Button(
            map_type.capitalize(),
            id=f"btn-{map_type}",
            n_clicks=0,
            className="m-1.5 px-3.5 py-1.5 text-base bg-blue-500 text-white rounded-lg shadow-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-50 transition duration-250 ease-in-out",
        )
        for map_type in map_types.keys()
    ],
    className="flex flex-wrap justify-center mb-6 bg-gray-100 p-3 rounded-xl shadow-lg",
)

# Create a container for the maps
map_container = html.Div(
    id="map-container",
    className="w-full max-w-3xl mx-auto bg-white rounded-xl shadow-xl overflow-hidden",
)

app.layout = html.Div(
    [
        html.H1(
            "Dash React Simple Maps",
            className="text-3xl font-bold text-center my-6 text-gray-800",
        ),
        map_buttons,
        map_container,
        html.Div(className="h-8"),  # Add extra space
        html.Div(
            html.Pre(
                "pip install dash-react-simple-maps",
                className="bg-black text-green-400 p-3 rounded-lg font-mono text-sm mx-auto",
            ),
            className="flex justify-center mb-6",
        ),
    ],
    className="min-h-screen bg-gradient-to-r from-blue-100 to-green-100 p-6",
)


@app.callback(
    Output("map-container", "children"),
    [Input(f"btn-{map_type}", "n_clicks") for map_type in map_types.keys()],
)
def update_map(*button_clicks):
    ctx = callback_context
    if not ctx.triggered:
        return map_types[DEFAULT_MAP]
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        map_type = button_id.split("-")[1]
        return map_types[map_type]


if __name__ == "__main__":
    app.run_server(debug=True)
