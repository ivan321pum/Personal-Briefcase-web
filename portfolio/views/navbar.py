import reflex as rx

import constants
from portfolio.styles.styles import Size
from portfolio.styles.colors import Color
from portfolio.components.link_button import navbar_link_button
from portfolio.styles.fonts import Font


def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.avatar(size="2"),
            rx.text(
                "Iván Sevilla Gómez",
                as_="b",
                font_size=Size.DEFAULT.value,
                color=Color.color_black.value,
                font_family=Font.DEFAULT.value,
            ),
        ),
        rx.spacer(),
        rx.hstack(
            rx.vstack(
                rx.hstack(
                    navbar_link_button("About Me", "", False),
                    navbar_link_button("My Skills", "", False),
                    navbar_link_button("Projects", "", False),
                    navbar_link_button("Contact me", "", False),
                ),
            ),
        ),
        position="sticky",
        bg=Color.color_white.value,
        border_bottom=f"0.15em solid {Color.color_black.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100",
    )
