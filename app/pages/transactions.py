import reflex as rx
from app.components.transactions_table import transactions_table
from app.components.add_transaction_modal import add_transaction_modal
from app.states.transaction_form_state import TransactionFormState


def transactions_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Transactions", class_name="text-3xl font-bold text-gray-900"),
            rx.el.button(
                "Add Transaction",
                on_click=TransactionFormState.open_dialog,
                class_name="px-4 py-2 bg-blue-500 text-white rounded-lg",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        transactions_table(),
        add_transaction_modal(),
        class_name="p-6",
    )