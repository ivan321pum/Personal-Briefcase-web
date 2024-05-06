import reflex as rx
import portfolio.styles.styles as styles  # importa el script de estilos
from portfolio.views.index.header import header
from portfolio.views.index.navbar import navbar
from portfolio.views.index.about_me import about_me
from portfolio.views.projects.projects import projects_views


def index() -> rx.Component:
    rx.script(src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.12.2/lottie.min.js")
    return rx.box(
        navbar(),
        header(),
        about_me(),
    )


def projects() -> rx.Component:
    return rx.box(
        navbar(),
        projects_views(),
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,  # añades los estilos a la app
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="Iván Sevilla, software developer",
    description="Software developer student"
)
app.add_page(
    projects,
    title="My projects",
    description="Showing of my projects"
)
