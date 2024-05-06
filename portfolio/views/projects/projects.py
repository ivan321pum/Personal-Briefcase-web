import reflex as rx

from reflex_intersection_observer import intersection_observer


def projects_views() -> rx.Component:
    return rx.box(
        rx.heading("MY PROJECTS"),
        intersection_observer(
            rx.card("Caca"),

        ),
    )
