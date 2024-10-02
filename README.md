<p align="center">
    <h1 align="center"><b>Dash React Simple Maps</b></h1>
	<p align="center">
		Beautiful maps for your Dash apps.
    <br />
    <br />
    <br />
    <img width="100" height="100" src="https://avatars.githubusercontent.com/u/60114551?s=200&v=4" alt="Ploomber Logo">
    <br />
    <b>  Made by <a href="https://ploomber.io/?utm_source=dash-react-simple-maps&utm_medium=github">Ploomber</a> with ❤️</b>
    <br />
    <br />
    <i>Deploy your Dash application on <a href="https://platform.ploomber.io/register/?utm_source=dash-react-simple-maps&utm_medium=github">Ploomber.io</a> for free.</i>
    <br />
  </p>
</p>
<br/>


https://github.com/user-attachments/assets/f849af08-09fd-4b48-9693-0292029ca7f5



Live demo: [dash-react-simple-maps.ploomberapp.io](https://dash-react-simple-maps.ploomberapp.io/)

## Installation

```sh
pip install dash-react-simple-maps
```

## Run demo locally

```sh
cd demo
pip install -r requirements.txt
python app.py
```

Open: http://localhost:8050


## Documentation

The `demo.py` file showcases various examples of using Dash React Simple Maps. Here's a breakdown of each map type:

1. Basic Map:
   A simple world map with basic styling.
   ```python
   map_basic = dash_react_simple_maps.DashReactSimpleMaps(
       id="map-basic",
       geoUrl=geoUrl,
       projection=ProjectionType.GEO_AZIMUTHAL_EQUAL_AREA,
       stroke="#6c757d",
       strokeWidth=1.0,
       fill="#f9f7f3",
   )
   ```

2. Styled Map:
   A map with custom styling for default and hover states.
   ```python
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
   ```

3. Map with Annotations:
   A map featuring text annotations for different continents.
   ```python
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
           # ... more annotations ...
       ],
       projection=ProjectionType.GEO_AZIMUTHAL_EQUIDISTANT,
       fill="#f9f7f3",
       stroke="#0fa3b1",
       strokeWidth=0.4,
   )
   ```

4. Map with Custom Projection Configuration:
   A map demonstrating custom projection settings.
   ```python
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
   ```

5. Map with Markers:
   A map showing various cities with custom markers.
   ```python
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
           # ... more markers ...
       ],
   )
   ```

6. Map with Lines:
   A map displaying lines connecting different locations.
   ```python
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
           # ... more lines ...
       ],
       geoUrl=geoUrl,
   )
   ```

7. Map with Color Property:
   A map that colors regions based on a specific property (population in this case).
   ```python
   map_colorproperty = dash_react_simple_maps.DashReactSimpleMaps(
       id="map-colorproperty",
       projection=ProjectionType.GEO_MERCATOR,
       geoUrl=geoUrl,
       colorProperty="POP2005",
       colorDomain=[0, 300_000_000],
       colorRange=["#FFF", "#06F"],
   )
   ```

8. Demo Map:
   A comprehensive map combining color property and custom styling.
   ```python
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
   ```

These examples demonstrate the versatility of Dash React Simple Maps, allowing for various customizations including projections, styling, annotations, markers, lines, and color-based visualizations.




## Setup

```sh
npm install
pip install -r requirements.txt
pip install -r tests/requirements.txt
```

## Development

```sh
npm run build
python demo/app.py
```


## Release

```sh
# generate
npm run build
python setup.py sdist bdist_wheel
ls dist

# test artifact
pip install dash dist/dash_react_simple_maps-0.0.1.tar.gz
python demo.py

# upload
pip install twine
twine upload dist/*

# clean up
rm -rf dist
```
