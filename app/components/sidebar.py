import reflex as rx
from app.states.auth_state import AuthState


def sidebar_item(
    text: str,
    icon: str,
    url: str | None = None,
    on_click: rx.event.EventHandler | None = None,
) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(icon, size=20),
            rx.el.span(text, class_name="font-medium"),
            class_name="flex items-center space-x-3",
        ),
        href=url,
        on_click=on_click,
        class_name="flex items-center px-4 py-2.5 text-gray-700 rounded-lg hover:bg-gray-100 cursor-pointer",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("bar-chart-2", size=32, class_name="text-violet-500"),
                    href="/",
                ),
                class_name="flex items-center mb-6",
            ),
            rx.el.nav(
                sidebar_item("Dashboard", "layout-grid", "/"),
                sidebar_item("Transactions", "arrow-left-right", "#"),
                sidebar_item("Accounts", "landmark", "#"),
                sidebar_item("Budgeting", "piggy-bank", "#"),
                sidebar_item("Settings", "settings", "#"),
                class_name="space-y-1",
            ),
            class_name="flex-1",
        ),
        rx.el.div(sidebar_item("Logout", "log-out", on_click=AuthState.sign_out)),
        class_name="flex flex-col h-full bg-white border-r border-gray-200 p-4 w-64",
    )