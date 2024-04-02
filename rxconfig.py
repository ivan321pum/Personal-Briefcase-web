import reflex as rx

config = rx.Config(
    app_name="portfolio",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)
