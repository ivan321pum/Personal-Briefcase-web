import reflex as rx
from portfolio.styles.fonts import Font
from portfolio.styles.styles import Size
from portfolio.styles.colors import Color
from portfolio.components.card import about_me_card

icon_size = "8em"


def programming() -> rx.box:
    return rx.box(
        rx.vstack(
            rx.text("Student Life"),
            rx.dialog.close(
                rx.button("Cierra")
            ),
        ),
    )


def about_me() -> rx.Component:
    return rx.box(
        rx.text("ABOUT ME", font_family=Font.TITLE.value, font_size=Size.VERY_BIG.value, align="center"),
        rx.flex(
            rx.grid(
                about_me_card(
                    text="PROGRAMMING PASSION",
                    color=Color.color_yellow.value,
                    dialog=programming,
                    img="/coding.svg",
                    img_size=icon_size,
                ),
                about_me_card(
                    text="STUDENT LIFE",
                    color=Color.color_green.value,
                    dialog=programming,
                    img="/student.svg",
                    img_size=icon_size,
                ),
                about_me_card(
                    text="PERSONAL GOALS",
                    img="/aim.svg",
                    dialog=programming,
                    color=Color.color_salmon.value,
                    img_size=icon_size,
                ),
                about_me_card(
                    text="PERSONALITY & INTERESTS",
                    color=Color.color_grey.value,
                    dialog=programming,
                    img="/stress.svg",
                    img_size=icon_size,
                ),
                columns="2",
                spacing="8",
                justify="center",
                width="60%",
            ),
            justify="center",
            align="center",
            width="100%",
            height="100%",
        ),
        id="about-me",
    )
