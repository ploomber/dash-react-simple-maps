# AUTO GENERATED FILE - DO NOT EDIT

export dashreactsimplemaps

"""
    dashreactsimplemaps(;kwargs...)

A DashReactSimpleMaps component.
DashReactSimpleMaps is a component that displays a world map.
It uses react-simple-maps to render the map and allows for annotations, lines, and markers.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `annotations` (optional): A list of annotations to be displayed on the map.. annotations has the following type: Array of lists containing elements 'coordinates', 'dx', 'dy', 'connectorProps', 'text', 'textColor'.
Those elements have the following types:
  - `coordinates` (Array of Reals; required)
  - `dx` (Real; optional)
  - `dy` (Real; optional)
  - `connectorProps` (Dict; optional)
  - `text` (String; required)
  - `textColor` (String; optional)s
- `colorDomain` (Array of Reals; optional): The domain for the color scale (tuple of two numbers).
- `colorProperty` (String; optional): The name of the property in the GeoJSON to use for coloring.
- `colorRange` (Array of Strings; optional): The range for the color scale (tuple of two color strings).
- `fill` (String; optional): The fill color of the map.
- `geoUrl` (String | Dict; optional): The URL or path to the GeoJSON or TopoJSON file.
- `lines` (optional): A list of lines to be displayed on the map.. lines has the following type: Array of lists containing elements 'from', 'to', 'stroke', 'strokeWidth', 'strokeLinecap'.
Those elements have the following types:
  - `from` (Array of Reals; required)
  - `to` (Array of Reals; required)
  - `stroke` (String; optional)
  - `strokeWidth` (Real; optional)
  - `strokeLinecap` (String; optional)s
- `markers` (optional): A list of markers to be displayed on the map.. markers has the following type: Array of lists containing elements 'name', 'coordinates', 'markerOffset', 'markerColor', 'textColor', 'fontSize', 'textStrokeColor', 'textStrokeWidth'.
Those elements have the following types:
  - `name` (String; required)
  - `coordinates` (Array of Reals; required)
  - `markerOffset` (Real; optional)
  - `markerColor` (String; optional)
  - `textColor` (String; optional)
  - `fontSize` (String; optional)
  - `textStrokeColor` (String; optional)
  - `textStrokeWidth` (Real; optional)s
- `projection` (String; optional): The projection to use for the map.
- `projectionConfig` (optional): Configuration for the map projection.. projectionConfig has the following type: lists containing elements 'rotate', 'center', 'scale'.
Those elements have the following types:
  - `rotate` (Array of Reals; optional)
  - `center` (Array of Reals; optional)
  - `scale` (Real; optional)
- `stroke` (String; optional): The color of the stroke for the map.
- `strokeWidth` (Real; optional): The width of the stroke for the map.
- `style` (optional): The style configuration for the Geography component.. style has the following type: lists containing elements 'default', 'hover', 'pressed'.
Those elements have the following types:
  - `default` (Dict; optional)
  - `hover` (Dict; optional)
  - `pressed` (Dict; optional)
"""
function dashreactsimplemaps(; kwargs...)
        available_props = Symbol[:id, :annotations, :colorDomain, :colorProperty, :colorRange, :fill, :geoUrl, :lines, :markers, :projection, :projectionConfig, :stroke, :strokeWidth, :style]
        wild_props = Symbol[]
        return Component("dashreactsimplemaps", "DashReactSimpleMaps", "dash_react_simple_maps", available_props, wild_props; kwargs...)
end

