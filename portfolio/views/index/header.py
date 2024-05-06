import reflex as rx
from reflex import Var
from portfolio.styles.colors import Color
from portfolio.styles.fonts import Font
from portfolio.styles.styles import Size
from portfolio.components.link_button import intern_button


class Spline(rx.Component):

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[
        str
    ] = "https://prod.spline.design/amVYWoGNiuhCRz3W/scene.splinecode"
    is_default = True

    lib_dependencies: list[str] = ["@splinetool/runtime"]


def spline_animation():
    return rx.center(
        Spline(),
        overflow="hidden",
        width="48em",
        height="48em",
    )


def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.vstack(
                    rx.text("Iván Sevilla", font_size="6em", font_family=Font.TITLE.value, weight="bold"),
                    rx.text("Exploring the ", rx.text.em("world "), "trough ", rx.text.em("code."), font_size="2em",),
                    intern_button("See projects", "", "4"),
                    padding_y="15em",
                    padding_x="10em",
                ),
            ),
            rx.spacer(),
            rx.flex(
                spline_animation(),
                justify="end",
                padding_x="1em"
            ),
        ),
        background=Color.color_red.value,
    )
