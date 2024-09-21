# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashReactSimpleMaps(Component):
    """A DashReactSimpleMaps component.
DashReactSimpleMaps is a component that displays a world map.
It uses react-simple-maps to render the map and allows for annotations, lines, and markers.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- annotations (list of dicts; optional):
    A list of annotations to be displayed on the map.

    `annotations` is a list of dicts with keys:

    - connectorProps (dict; optional)

    - coordinates (list of numbers; required)

    - dx (number; optional)

    - dy (number; optional)

    - text (string; required)

    - textColor (string; optional)

- colorDomain (list of numbers; optional):
    The domain for the color scale (tuple of two numbers).

- colorProperty (string; optional):
    The name of the property in the GeoJSON to use for coloring.

- colorRange (list of strings; optional):
    The range for the color scale (tuple of two color strings).

- fill (string; optional):
    The fill color of the map.

- geoUrl (string | dict; default "https://raw.githubusercontent.com/MinnPost/simple-map-d3/refs/heads/master/example-data/world-population.geo.json"):
    The URL or path to the GeoJSON or TopoJSON file.

- lines (list of dicts; optional):
    A list of lines to be displayed on the map.

    `lines` is a list of dicts with keys:

    - from (list of numbers; required)

    - stroke (string; optional)

    - strokeLinecap (string; optional)

    - strokeWidth (number; optional)

    - to (list of numbers; required)

- markers (list of dicts; optional):
    A list of markers to be displayed on the map.

    `markers` is a list of dicts with keys:

    - coordinates (list of numbers; required)

    - fontSize (string; optional)

    - markerColor (string; optional)

    - markerOffset (number; optional)

    - name (string; required)

    - textColor (string; optional)

    - textStrokeColor (string; optional)

    - textStrokeWidth (number; optional)

- projection (string; default "geoMercator"):
    The projection to use for the map.

- projectionConfig (dict; optional):
    Configuration for the map projection.

    `projectionConfig` is a dict with keys:

    - center (list of numbers; optional)

    - rotate (list of numbers; optional)

    - scale (number; optional)

- stroke (string; optional):
    The color of the stroke for the map.

- strokeWidth (number; optional):
    The width of the stroke for the map.

- style (dict; optional):
    The style configuration for the Geography component.

    `style` is a dict with keys:

    - default (dict; optional)

    - hover (dict; optional)

    - pressed (dict; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_react_simple_maps'
    _type = 'DashReactSimpleMaps'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, annotations=Component.UNDEFINED, lines=Component.UNDEFINED, markers=Component.UNDEFINED, projectionConfig=Component.UNDEFINED, projection=Component.UNDEFINED, style=Component.UNDEFINED, geoUrl=Component.UNDEFINED, colorProperty=Component.UNDEFINED, colorDomain=Component.UNDEFINED, colorRange=Component.UNDEFINED, stroke=Component.UNDEFINED, strokeWidth=Component.UNDEFINED, fill=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'annotations', 'colorDomain', 'colorProperty', 'colorRange', 'fill', 'geoUrl', 'lines', 'markers', 'projection', 'projectionConfig', 'stroke', 'strokeWidth', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'annotations', 'colorDomain', 'colorProperty', 'colorRange', 'fill', 'geoUrl', 'lines', 'markers', 'projection', 'projectionConfig', 'stroke', 'strokeWidth', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashReactSimpleMaps, self).__init__(**args)
