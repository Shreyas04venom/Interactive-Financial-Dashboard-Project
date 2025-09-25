import reflex as rx
from app.states.auth_state import AuthState
from app.states.dashboard_state import DashboardState


def sidebar_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(icon, size=20),
            rx.el.span(text, class_name="font-medium"),
            class_name="flex items-center space-x-3",
        ),
        href=url,
        class_name=rx.cond(
            DashboardState.active_page == text.lower(),
            "flex items-center px-4 py-2.5 text-white bg-indigo-600 rounded-lg cursor-pointer",
            "flex items-center px-4 py-2.5 text-gray-700 rounded-lg hover:bg-gray-100 cursor-pointer",
        ),
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.icon("bar-chart-big", size=32, class_name="text-indigo-600"),
                    href="/",
                ),
                class_name="flex items-center mb-8",
            ),
            rx.el.nav(
                sidebar_item("Dashboard", "layout-dashboard", "/"),
                sidebar_item("Transactions", "arrow-left-right", "/transactions"),
                sidebar_item("Accounts", "landmark", "/accounts"),
                sidebar_item("Budgeting", "piggy-bank", "/budgeting"),
                sidebar_item("Settings", "settings", "/settings"),
                class_name="space-y-2",
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.image(
                        src=f"https://api.dicebear.com/9.x/notionists/svg?seed={AuthState.user_email}",
                        class_name="w-10 h-10 rounded-full",
                    ),
                    rx.el.div(
                        rx.el.p("Admin", class_name="font-semibold text-sm"),
                        rx.el.p(
                            AuthState.user_email, class_name="text-xs text-gray-500"
                        ),
                        class_name="flex flex-col",
                    ),
                    class_name="flex items-center gap-3",
                ),
                rx.el.button(
                    rx.icon("log-out", size=20),
                    on_click=AuthState.sign_out,
                    class_name="text-gray-500 hover:text-gray-800",
                    background="transparent",
                ),
                class_name="flex items-center justify-between p-3 bg-gray-100 rounded-lg",
            )
        ),
        class_name="flex flex-col h-screen bg-white border-r border-gray-200 p-4 w-72",
    )