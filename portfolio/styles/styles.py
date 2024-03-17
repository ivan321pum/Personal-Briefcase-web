import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color

class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    BIG = "2em"
    VERY_BIG = "4em"


STYLESHEETS = [
    "https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css",
    "https://fonts.googleapis.com/css2?family=Roboto&display=swap",
    "https://fonts.googleapis.com/css2?family=Julius+Sans+One&display=swap",
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": Color.color_black.value,
    "background": Color.color_white.value,
    "font_size": Size.DEFAULT.value
}
