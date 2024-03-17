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
        width="50em",
        height="50em",
    )


def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.box(
                    rx.text("Iván Sevilla", font_size="5em", font_family=Font.TITLE.value, weight="bold"),
                    rx.text("Exploring the world trough code.", size="5"),
                    intern_button("See projects", "", "4"),
                    padding_y="15em",
                    padding_x="10em",
                ),
            ),
            rx.spacer(),  # Esto empujará el Spline hacia la derecha
            rx.flex(
                spline_animation(),
                justify="end",
            ),
        ),
        background=Color.color_red.value,
    )