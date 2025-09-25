import reflex as rx
from app.states.auth_state import AuthState
from app.states.dashboard_state import DashboardState


def sidebar_item(text: str, icon: str, page: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=20),
            rx.el.span(text, class_name="font-medium"),
            class_name="flex items-center space-x-3",
        ),
        on_click=lambda: DashboardState.set_active_page(page),
        class_name=rx.cond(
            DashboardState.active_page == page,
            "flex items-center px-4 py-2.5 text-white bg-violet-500 rounded-lg cursor-pointer",
            "flex items-center px-4 py-2.5 text-gray-700 rounded-lg hover:bg-gray-100 cursor-pointer",
        ),
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
                sidebar_item("Dashboard", "layout-grid", "Dashboard"),
                sidebar_item("Transactions", "arrow-left-right", "Transactions"),
                sidebar_item("Accounts", "landmark", "Accounts"),
                sidebar_item("Budgeting", "piggy-bank", "Budgeting"),
                sidebar_item("Settings", "settings", "Settings"),
                class_name="space-y-1",
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("log-out", size=20),
                rx.el.span("Logout", class_name="font-medium"),
                class_name="flex items-center space-x-3",
            ),
            on_click=AuthState.sign_out,
            class_name="flex items-center px-4 py-2.5 text-gray-700 rounded-lg hover:bg-gray-100 cursor-pointer",
        ),
        class_name="flex flex-col h-full bg-white border-r border-gray-200 p-4 w-64",
    )