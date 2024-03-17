import reflex as rx

from portfolio.styles.styles import Size


def header() -> rx.Component:
    return rx.vstack(
        rx.heading(),
        rx.flex(
            rx.avatar(fallback="YO", size="9"),
            rx.box(
                rx.text("Lorem impsum dolor sit aemet"),
                rx.text("Lorem impsum dolor sit aemet"),
            ),
        ),
        rx.icon(tag="chevron_down", width=Size.VERY_BIG.value, height=Size.VERY_BIG.value),
    )
