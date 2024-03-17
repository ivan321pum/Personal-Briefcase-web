import reflex as rx
from portfolio.styles.colors import Color
from portfolio.styles.fonts import Font
from portfolio.styles.styles import Size


def header() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("Iván Sevilla", font_size=Size.VERY_BIG.value, font_family=Font.TITLE.value, weight="bold"),
            rx.text("Explorando el mundo a través del código.", size="5"),
        ),
        background_color=Color.color_red.value,
        padding_y="15em",
        padding_x="5em",
    )
