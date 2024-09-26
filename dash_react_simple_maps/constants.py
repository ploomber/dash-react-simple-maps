from enum import Enum


class ProjectionType(str, Enum):
    def __new__(cls, value):
        obj = str.__new__(cls, value)
        obj._value_ = value
        return obj

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"ProjectionType.{self.name}"

    GEO_EQUAL_EARTH = "geoEqualEarth"
    GEO_ALBERS = "geoAlbers"
    GEO_ALBERS_USA = "geoAlbersUsa"
    GEO_AZIMUTHAL_EQUAL_AREA = "geoAzimuthalEqualArea"
    GEO_AZIMUTHAL_EQUIDISTANT = "geoAzimuthalEquidistant"
    GEO_ORTHOGRAPHIC = "geoOrthographic"
    GEO_CONIC_CONFORMAL = "geoConicConformal"
    GEO_CONIC_EQUAL_AREA = "geoConicEqualArea"
    GEO_CONIC_EQUIDISTANT = "geoConicEquidistant"
    GEO_STEREOGRAPHIC = "geoStereographic"
    GEO_MERCATOR = "geoMercator"
    GEO_TRANSVERSE_MERCATOR = "geoTransverseMercator"


from typing import List, Dict, Any


class ProjectionConfig(Dict[str, Any]):
    def __init__(
        self,
        rotate: List[float] = [0, 0, 0],
        center: List[float] = [0, 0],
        scale: float = 0,
    ):
        super().__init__()
        self["rotate"] = rotate
        self["center"] = center
        self["scale"] = scale

    @property
    def rotate(self) -> List[float]:
        """Rotation of the projection"""
        return self["rotate"]

    @rotate.setter
    def rotate(self, value: List[float]):
        self["rotate"] = value

    @property
    def center(self) -> List[float]:
        """Center of the projection"""
        return self["center"]

    @center.setter
    def center(self, value: List[float]):
        self["center"] = value

    @property
    def scale(self) -> float:
        """Scale of the projection"""
        return self["scale"]

    @scale.setter
    def scale(self, value: float):
        self["scale"] = value


class Style(Dict[str, Any]):
    def __init__(
        self,
        default: Dict[str, str] = {"fill": "#EEE"},
        hover: Dict[str, str] = {"fill": "#0000FF"},
        pressed: Dict[str, str] = {"fill": "#E42"},
    ):
        super().__init__()
        self["default"] = default
        self["hover"] = hover
        self["pressed"] = pressed

    @property
    def default(self) -> Dict[str, str]:
        """Default style for geography"""
        return self["default"]

    @default.setter
    def default(self, value: Dict[str, str]):
        self["default"] = value

    @property
    def hover(self) -> Dict[str, str]:
        """Hover style for geography"""
        return self["hover"]

    @hover.setter
    def hover(self, value: Dict[str, str]):
        self["hover"] = value

    @property
    def pressed(self) -> Dict[str, str]:
        """Pressed style for geography"""
        return self["pressed"]

    @pressed.setter
    def pressed(self, value: Dict[str, str]):
        self["pressed"] = value
