import reflex as rx
from portfolio.styles.fonts import Font
from portfolio.styles.styles import Size
from portfolio.styles.colors import Color


def about_me() -> rx.Component:
    return rx.box(
        rx.text("ABOUT ME", font_family=Font.TITLE.value, font_size=Size.BIG.value, align="center"),
        rx.flex(
            rx.card(
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.link(
                            rx.box(
                                "CODING",
                                background="center/cover url('https://i.blogs.es/fd396a/hook/450_1000.jpg')",
                            ),
                        )
                    ),
                    rx.dialog.content(
                        rx.vstack(
                            rx.text("MI PASIÓN POR EL CÓDIGO", as_="p"),
                            rx.dialog.close(
                                rx.button("Cierra")
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
