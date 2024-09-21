% Auto-generated: do not edit by hand
\name{dashReactSimpleMaps}

\alias{dashReactSimpleMaps}

\title{DashReactSimpleMaps component}

\description{
DashReactSimpleMaps is a component that displays a world map. It uses react-simple-maps to render the map and allows for annotations, lines, and markers.
}

\usage{
dashReactSimpleMaps(id=NULL, annotations=NULL, colorDomain=NULL,
colorProperty=NULL, colorRange=NULL, fill=NULL, geoUrl=NULL,
lines=NULL, markers=NULL, projection=NULL,
projectionConfig=NULL, stroke=NULL, strokeWidth=NULL,
style=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{annotations}{List of lists containing elements 'coordinates', 'dx', 'dy', 'connectorprops', 'text', 'textcolor'.
those elements have the following types:
  - coordinates (list of numerics; required)
  - dx (numeric; optional)
  - dy (numeric; optional)
  - connectorprops (named list; optional)
  - text (character; required)
  - textcolor (character; optional)s. A list of annotations to be displayed on the map.}

\item{colorDomain}{List of numerics. The domain for the color scale (tuple of two numbers).}

\item{colorProperty}{Character. The name of the property in the GeoJSON to use for coloring.}

\item{colorRange}{List of characters. The range for the color scale (tuple of two color strings).}

\item{fill}{Character. The fill color of the map.}

\item{geoUrl}{Character | named list. The URL or path to the GeoJSON or TopoJSON file.}

\item{lines}{List of lists containing elements 'from', 'to', 'stroke', 'strokewidth', 'strokelinecap'.
those elements have the following types:
  - from (list of numerics; required)
  - to (list of numerics; required)
  - stroke (character; optional)
  - strokewidth (numeric; optional)
  - strokelinecap (character; optional)s. A list of lines to be displayed on the map.}

\item{markers}{List of lists containing elements 'name', 'coordinates', 'markeroffset', 'markercolor', 'textcolor', 'fontsize', 'textstrokecolor', 'textstrokewidth'.
those elements have the following types:
  - name (character; required)
  - coordinates (list of numerics; required)
  - markeroffset (numeric; optional)
  - markercolor (character; optional)
  - textcolor (character; optional)
  - fontsize (character; optional)
  - textstrokecolor (character; optional)
  - textstrokewidth (numeric; optional)s. A list of markers to be displayed on the map.}

\item{projection}{Character. The projection to use for the map.}

\item{projectionConfig}{Lists containing elements 'rotate', 'center', 'scale'.
those elements have the following types:
  - rotate (list of numerics; optional)
  - center (list of numerics; optional)
  - scale (numeric; optional). Configuration for the map projection.}

\item{stroke}{Character. The color of the stroke for the map.}

\item{strokeWidth}{Numeric. The width of the stroke for the map.}

\item{style}{Lists containing elements 'default', 'hover', 'pressed'.
those elements have the following types:
  - default (named list; optional)
  - hover (named list; optional)
  - pressed (named list; optional). The style configuration for the Geography component.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

