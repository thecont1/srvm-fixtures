"""Minimal Reflex app — detected by srvm via rxconfig.py."""

import reflex as rx


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("srvm fixture x12 - reflex"),
            rx.text("Detected via rxconfig.py; launched with `reflex run`."),
        )
    )


app = rx.App()
app.add_page(index)
