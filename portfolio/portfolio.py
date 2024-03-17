import reflex as rx
import portfolio.styles.styles as styles  # importa el script de estilos
from portfolio.views.header import header
from portfolio.views.navbar import navbar


def index() -> rx.Component:
    rx.script(src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.12.2/lottie.min.js")
    return rx.box(
        navbar(),
        header(),
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,  # añades los estilos a la app
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="Iván Sevilla, software developer",
    description="Prueba"
)
