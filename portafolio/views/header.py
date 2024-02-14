import reflex as rx
import reflex.components.radix.themes as rdxt

from portafolio.styles.styles import Size

def header() -> rx.component:
    return rx.vstack(
        rx.heading(),
        rx.flex(
            rdxt.avatar(fallback="YO", size=Size.VERY_BIG.value),
            rx.box(
                rx.text("Lorem impsum dolor sit aemet"),
                rx.text("Lorem impsum dolor sit aemet"),
            ),
        ),
    rx.icon(tag="chevron_down", width=Size.VERY_BIG.value, height=Size.VERY_BIG.value),
    )
