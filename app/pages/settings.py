import reflex as rx
from app.components.sidebar import sidebar


def settings_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1("Settings", class_name="text-3xl font-bold text-gray-900"),
                class_name="p-8",
            ),
            class_name="flex-1 bg-gray-50",
        ),
        class_name="flex h-screen font-['Inter'] bg-gray-50",
    )