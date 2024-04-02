import reflex as rx
from portfolio.styles.colors import Color
from typing import Callable


def about_me_card(text: str, img: str, dialog: Callable[[], rx.box], color: str, img_size: str):
    return rx.card(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.link(
                    rx.box(
                        rx.vstack(
                            rx.image(src=img, width=img_size, height="auto", ),
                            rx.heading(text, as_="h1", align="center", style={"color": Color.color_black.value}),
                            align="center",
                            justify="center",
                        ),
                    ),
                ),
            ),
            rx.dialog.content(
                dialog()
            ),
        ),
        background=color,
    )
