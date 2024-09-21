import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { ComposableMap, Geographies, Geography, Annotation, ZoomableGroup, Graticule, Line, Marker } from "react-simple-maps";
import { scaleLinear } from "d3-scale"
import ReactTooltip from 'react-tooltip';

/**
 * DashReactSimpleMaps is a component that displays a world map.
 * It uses react-simple-maps to render the map and allows for annotations, lines, and markers.
 */

const DashReactSimpleMaps = (props) => {
    const { id, annotations, projectionConfig, projection, style, lines, geoUrl, colorProperty, colorDomain, colorRange, markers, stroke, strokeWidth, fill } = props;
    const activeColorScale = colorDomain && colorRange
        ? scaleLinear().domain(colorDomain).range(colorRange)
        : null;

    const [tooltipContent, setTooltipContent] = useState("");

    useEffect(() => {
        ReactTooltip.rebuild();
    }, [tooltipContent]);

    return (
        <div id={id} data-tip="">
            <ComposableMap
                projection={projection}
                projectionConfig={projectionConfig}
            >
                <ZoomableGroup>
                    <Graticule stroke="#DDD" />
                    <Geographies geography={geoUrl}>
                        {({ geographies }) =>
                            geographies.map((geo) => (
                                <Geography
                                    key={geo.rsmKey}
                                    geography={geo}
                                    fill={colorProperty ? activeColorScale(geo.properties[colorProperty]) : fill}
                                    {...(stroke && { stroke })}
                                    {...(strokeWidth && { strokeWidth })}
                                    style={style}
                                    onMouseEnter={() => {
                                        if (colorProperty && geo.properties[colorProperty]) {
                                            setTooltipContent(`${colorProperty}: ${Number(geo.properties[colorProperty]).toLocaleString()}`);
                                        } else {
                                            setTooltipContent("");
                                        }
                                    }}
                                    onMouseLeave={() => {
                                        setTooltipContent("");
                                    }}
                                />
                            ))
                        }
                    </Geographies>
                    {annotations.map((annotation, index) => (
                        <Annotation
                            key={index}
                            subject={annotation.coordinates}
                            dx={annotation.dx}
                            dy={annotation.dy}
                            connectorProps={annotation.connectorProps}
                        >
                            <text x="-8" textAnchor="end" alignmentBaseline="middle" fill={annotation.textColor || "#F53"} style={{ fontFamily: "system-ui" }}>
                                {annotation.text}
                            </text>
                        </Annotation>
                    ))}
                    {lines.map((line, index) => (
                        <Line
                            key={index}
                            from={line.from}
                            to={line.to}
                            stroke={line.stroke || "#FF5533"}
                            strokeWidth={line.strokeWidth || 2}
                            strokeLinecap={line.strokeLinecap || "round"}
                        />
                    ))}
                    {markers.map(({ name, coordinates, markerOffset, markerColor, textColor, fontSize, textStrokeColor, textStrokeWidth }) => (
                        <Marker key={name} coordinates={coordinates}>
                            <g
                                fill="none"
                                stroke={markerColor || "#FF5533"}
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                transform="translate(-12, -24)"
                            >
                                <circle cx="12" cy="10" r="3" />
                                <path d="M12 21.7C17.3 17 20 13 20 10a8 8 0 1 0-16 0c0 3 2.7 6.9 8 11.7z" />
                            </g>
                            <text
                                textAnchor="middle"
                                y={markerOffset}
                                style={{
                                    fontFamily: "system-ui",
                                    fill: textColor || "#5D5A6D",
                                    fontSize: fontSize || "14px",
                                    stroke: textStrokeColor,
                                    strokeWidth: textStrokeWidth
                                }}
                            >
                                {name}
                            </text>
                        </Marker>
                    ))}
                </ZoomableGroup>
            </ComposableMap>
            <ReactTooltip>{tooltipContent}</ReactTooltip>
        </div>
    );
}

DashReactSimpleMaps.defaultProps = {
    annotations: [],
    lines: [],
    markers: [],
    projection: "geoMercator",
    geoUrl: "https://raw.githubusercontent.com/MinnPost/simple-map-d3/refs/heads/master/example-data/world-population.geo.json",
    colorProperty: null,
    colorDomain: null,
    colorRange: null,
};

DashReactSimpleMaps.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    /**
     * A list of annotations to be displayed on the map.
     */
    annotations: PropTypes.arrayOf(PropTypes.shape({
        coordinates: PropTypes.arrayOf(PropTypes.number).isRequired,
        dx: PropTypes.number,
        dy: PropTypes.number,
        connectorProps: PropTypes.object,
        text: PropTypes.string.isRequired,
        textColor: PropTypes.string
    })),
    /**
     * A list of lines to be displayed on the map.
     */
    lines: PropTypes.arrayOf(PropTypes.shape({
        from: PropTypes.arrayOf(PropTypes.number).isRequired,
        to: PropTypes.arrayOf(PropTypes.number).isRequired,
        stroke: PropTypes.string,
        strokeWidth: PropTypes.number,
        strokeLinecap: PropTypes.string
    })),
    /**
     * A list of markers to be displayed on the map.
     */
    markers: PropTypes.arrayOf(PropTypes.shape({
        name: PropTypes.string.isRequired,
        coordinates: PropTypes.arrayOf(PropTypes.number).isRequired,
        markerOffset: PropTypes.number,
        markerColor: PropTypes.string,
        textColor: PropTypes.string,
        fontSize: PropTypes.string,
        textStrokeColor: PropTypes.string,
        textStrokeWidth: PropTypes.number
    })),
    /**
     * Configuration for the map projection.
     */
    projectionConfig: PropTypes.shape({
        rotate: PropTypes.arrayOf(PropTypes.number),
        center: PropTypes.arrayOf(PropTypes.number),
        scale: PropTypes.number
    }),
    /**
     * The projection to use for the map.
     */
    projection: PropTypes.string,
    /**
     * The style configuration for the Geography component.
     */
    style: PropTypes.shape({
        default: PropTypes.object,
        hover: PropTypes.object,
        pressed: PropTypes.object
    }),
    /**
     * The URL or path to the GeoJSON or TopoJSON file.
     */
    geoUrl: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),
    /**
     * The name of the property in the GeoJSON to use for coloring.
     */
    colorProperty: PropTypes.string,
    /**
     * The domain for the color scale (tuple of two numbers).
     */
    colorDomain: PropTypes.arrayOf(PropTypes.number),
    /**
     * The range for the color scale (tuple of two color strings).
     */
    colorRange: PropTypes.arrayOf(PropTypes.string),
    /**
     * The color of the stroke for the map.
     */
    stroke: PropTypes.string,
    /**
     * The width of the stroke for the map.
     */
    strokeWidth: PropTypes.number,
    /**
     * The fill color of the map.
     */
    fill: PropTypes.string
};

export default DashReactSimpleMaps;
