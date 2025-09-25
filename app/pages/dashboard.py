import reflex as rx
from app.components.sidebar import sidebar
from app.components.net_worth_chart import net_worth_chart
from app.components.portfolio_allocation_chart import portfolio_allocation_chart
from app.components.transactions_table import transactions_table
from app.states.auth_state import AuthState
from app.states.dashboard_state import DashboardState
from app.pages.transactions import transactions_page
from app.pages.accounts import accounts_page
from app.pages.budgeting import budgeting_page
from app.pages.settings import settings_page


def dashboard_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1("Dashboard", class_name="text-3xl font-bold text-gray-900"),
        rx.el.div(
            net_worth_chart(),
            portfolio_allocation_chart(),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6 my-6",
        ),
        transactions_table(),
        class_name="p-6",
    )


def dashboard() -> rx.Component:
    return rx.el.div(
        rx.cond(
            AuthState.in_session,
            rx.el.div(
                sidebar(),
                rx.el.main(
                    rx.match(
                        DashboardState.active_page,
                        ("Dashboard", dashboard_content()),
                        ("Transactions", transactions_page()),
                        ("Accounts", accounts_page()),
                        ("Budgeting", budgeting_page()),
                        ("Settings", settings_page()),
                        dashboard_content(),
                    ),
                    class_name="flex-1 bg-gray-50",
                ),
                class_name="flex h-screen font-['Inter']",
            ),
            rx.el.div(
                rx.el.h1("Loading...", class_name="text-2xl font-bold"),
                class_name="flex flex-col items-center justify-center h-screen bg-gray-100 gap-4",
            ),
        )
    )