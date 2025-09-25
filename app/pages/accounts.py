import reflex as rx


def accounts_page() -> rx.Component:
    return rx.el.div(
        rx.el.h1("Accounts", class_name="text-3xl font-bold text-gray-900"),
        class_name="p-6",
    )