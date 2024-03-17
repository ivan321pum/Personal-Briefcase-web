import reflex as rx

import constants
from portfolio.styles.styles import Size
from portfolio.styles.colors import Color, TextColor
from portfolio.components.link_button import navbar_link_button, icon_button


def updated_navbar() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Iván Sevilla Gómez",
                as_="b",
                font_size=Size.VERY_BIG.value,
                color=TextColor.title.value
            ),
        ),
    )
