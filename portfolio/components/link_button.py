import reflex as rx
from portfolio.styles.styles import Size
from portfolio.styles.colors import Color
from portfolio.styles.fonts import Font


def navbar_link_button(text: str, url: str, external: bool):
    return rx.link(
        text,
        color=Color.color_black.value,
        size="3",
        href=url,
        button=True,
        is_external=external,
        padding_x=Size.DEFAULT.value,
        font_family=Font.DEFAULT.value,
    )


def icon_button(img: str, url: str, external: bool):
    return rx.link(
        rx.button(
            rx.image(
                src=img,
                width=Size.BIG.value,
                height=Size.BIG.value,
            )
        ),
        href=url,
        button=True,
        is_external=external,
    )
