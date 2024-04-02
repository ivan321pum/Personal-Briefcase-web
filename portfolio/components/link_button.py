import reflex as rx
from portfolio.styles.styles import Size
from portfolio.styles.colors import Color
from portfolio.styles.fonts import Font
from reflex_simpleicons import simpleicons


def navbar_link_button(text: str, url: str, external: bool):
    return rx.link(
        rx.text(text),
        color=Color.color_black.value,
        size="3",
        href=url,
        button=True,
        is_external=external,
        padding_x=Size.DEFAULT.value,
        font_family=Font.DEFAULT.value,
    )


def navbar_link_format_button(text: str, url: str, external: bool, format: str):
    return rx.link(
        rx.text(text, as_=format),
        color=Color.color_black.value,
        size="3",
        href=url,
        button=True,
        is_external=external,
        padding_x=Size.DEFAULT.value,
        font_family=Font.DEFAULT.value,
        class_name="scroll-smooth"
    )


def icon_button(icon: str, url: str, external: bool):
    return rx.link(
        simpleicons(icon, size=30),
        color=Color.color_black.value,
        size="3",
        href=url,
        button=True,
        is_external=external,
        padding_x=Size.DEFAULT.value,
        font_family=Font.DEFAULT.value,
    )


def intern_button(text: str, url: str, size: str):
    return rx.link(
        rx.button(
            text,
            font_family=Font.DEFAULT.value,
            color=Color.color_blue.value,
            size=size,
            text_color=Color.color_black.value,
        ),
        scr=url,
        is_external=False,
        padding_y="0.5em",
    )
