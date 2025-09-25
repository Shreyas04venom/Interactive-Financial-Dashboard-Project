import reflex as rx
from app.components.sidebar import sidebar
from app.components.net_worth_chart import net_worth_chart
from app.components.portfolio_allocation_chart import portfolio_allocation_chart
from app.components.transactions_table import transactions_table
from app.states.auth_state import AuthState
from app.states.dashboard_state import DashboardState


def dashboard_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Welcome back, Admin!", class_name="text-3xl font-bold text-gray-900"
            ),
            rx.el.p(
                "Here's your financial overview for today.",
                class_name="text-gray-600 mt-1",
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            net_worth_chart(),
            portfolio_allocation_chart(),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 my-6",
        ),
        transactions_table(),
        class_name="p-8",
    )


def dashboard() -> rx.Component:
    return rx.el.div(
        rx.cond(
            AuthState.in_session,
            rx.el.div(
                sidebar(),
                rx.el.main(dashboard_content(), class_name="flex-1 bg-gray-50"),
                class_name="flex h-screen font-['Inter'] bg-gray-50",
            ),
            rx.el.div(
                rx.el.h1("Loading...", class_name="text-2xl font-bold"),
                class_name="flex flex-col items-center justify-center h-screen bg-gray-100 gap-4",
            ),
        )
    )