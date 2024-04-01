import reflex as rx
from portfolio.styles.fonts import Font
from portfolio.styles.styles import Size
from portfolio.styles.colors import Color


def about_me() -> rx.Component:
    return rx.box(
        rx.text("ABOUT ME", font_family=Font.TITLE.value, font_size=Size.VERY_BIG.value, align="center"),
        rx.flex(
            rx.grid(
                rx.card(
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.link(
                                rx.box(
                                    rx.heading("PROGRAMMING PASSION", as_="h1", align="center", style={"color": Color.color_black.value}),
                                ),
                            ),
                        ),
                        rx.dialog.content(
                            rx.vstack(
                                rx.text("Student Life"),
                                rx.dialog.close(
                                    rx.button("Cierra")
                                ),
                            ),
                        ),
                    ),
                    background=Color.color_yellow.value,
                ),
                rx.card(
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.link(
                                rx.box(
                                    rx.heading("STUDENT LIFE", as_="h1", align="center", style={"color": Color.color_black.value}),
                                ),
                            )
                        ),
                        rx.dialog.content(
                            rx.vstack(
                                rx.text("MI PASIÓN POR EL CÓDIGO"),
                                rx.dialog.close(
                                    rx.button("Cierra")
                                ),
                            ),
                        ),
                    ),
                    background=Color.color_green.value,
                ),
                rx.card(
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.link(
                                rx.box(
                                    rx.heading("PERSONAL GOALS", as_="h1", align="center", style={"color": Color.color_black.value}),
                                ),
                            )
                        ),
                        rx.dialog.content(
                            rx.vstack(
                                rx.text("MI PASIÓN POR EL CÓDIGO"),
                                rx.dialog.close(
                                    rx.button("Cierra")
                                ),
                            ),
                        ),
                    ),
                    background=Color.color_salmon.value,
                ),
                rx.card(
                    rx.dialog.root(
                        rx.dialog.trigger(
                            rx.link(
                                rx.box(
                                    rx.heading("PERSONALITY & INTERESTS", as_="h1", align="center", style={"color": Color.color_black.value}),
                                ),
                            )
                        ),
                        rx.dialog.content(
                            rx.vstack(
                                rx.text("MI PASIÓN POR EL CÓDIGO"),
                                rx.dialog.close(
                                    rx.button("Cierra")
                                ),
                            ),
                        ),
                    ),
                    background=Color.color_grey.value,
                ),
                columns="2",
                spacing="8",
                justify="center",
                width="50%",
            ),
            justify="center",
            align="center",
            width="100%",
            height="100%",
        ),
    )
