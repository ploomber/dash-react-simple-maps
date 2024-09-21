# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashReactSimpleMaps <- function(id=NULL, annotations=NULL, colorDomain=NULL, colorProperty=NULL, colorRange=NULL, fill=NULL, geoUrl=NULL, lines=NULL, markers=NULL, projection=NULL, projectionConfig=NULL, stroke=NULL, strokeWidth=NULL, style=NULL) {
    
    props <- list(id=id, annotations=annotations, colorDomain=colorDomain, colorProperty=colorProperty, colorRange=colorRange, fill=fill, geoUrl=geoUrl, lines=lines, markers=markers, projection=projection, projectionConfig=projectionConfig, stroke=stroke, strokeWidth=strokeWidth, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashReactSimpleMaps',
        namespace = 'dash_react_simple_maps',
        propNames = c('id', 'annotations', 'colorDomain', 'colorProperty', 'colorRange', 'fill', 'geoUrl', 'lines', 'markers', 'projection', 'projectionConfig', 'stroke', 'strokeWidth', 'style'),
        package = 'dashReactSimpleMaps'
        )

    structure(component, class = c('dash_component', 'list'))
}
