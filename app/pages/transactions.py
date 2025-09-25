import reflex as rx
from app.components.sidebar import sidebar
from app.components.transactions_table import transactions_table
from app.components.add_transaction_modal import add_transaction_modal
from app.states.transaction_form_state import TransactionFormState


def transactions_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h1(
                            "Transactions",
                            class_name="text-3xl font-bold text-gray-900",
                        ),
                        rx.el.p(
                            "View and manage all your financial transactions.",
                            class_name="text-gray-600 mt-1",
                        ),
                    ),
                    rx.el.button(
                        rx.icon(tag="plus", class_name="mr-2"),
                        "Add Transaction",
                        on_click=TransactionFormState.open_dialog,
                        class_name="flex items-center px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700",
                    ),
                    class_name="flex justify-between items-center mb-8",
                ),
                transactions_table(title="All Transactions"),
                add_transaction_modal(),
                class_name="p-8",
            ),
            class_name="flex-1 bg-gray-50",
        ),
        class_name="flex h-screen font-['Inter'] bg-gray-50",
    )