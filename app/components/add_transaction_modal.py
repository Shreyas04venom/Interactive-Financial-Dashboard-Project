import reflex as rx
from app.states.transaction_form_state import TransactionFormState


def add_transaction_modal() -> rx.Component:
    return rx.el.dialog(
        rx.el.div(
            rx.el.div(
                rx.el.h2("Add Transaction", class_name="text-xl font-bold mb-4"),
                rx.el.form(
                    rx.el.div(
                        rx.el.label("Date", class_name="text-sm font-medium"),
                        rx.el.input(
                            name="date",
                            type="date",
                            required=True,
                            class_name="w-full p-2 border rounded",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label("Description", class_name="text-sm font-medium"),
                        rx.el.input(
                            name="description",
                            required=True,
                            class_name="w-full p-2 border rounded",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label("Amount", class_name="text-sm font-medium"),
                        rx.el.input(
                            name="amount",
                            type="number",
                            step="0.01",
                            required=True,
                            class_name="w-full p-2 border rounded",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label("Type", class_name="text-sm font-medium"),
                        rx.el.select(
                            rx.el.option("income", value="income"),
                            rx.el.option("expense", value="expense"),
                            rx.el.option("investment", value="investment"),
                            name="type",
                            required=True,
                            class_name="w-full p-2 border rounded",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Cancel",
                            type="button",
                            on_click=TransactionFormState.close_dialog,
                            class_name="mr-2 px-4 py-2 bg-gray-300 rounded",
                        ),
                        rx.el.button(
                            "Add",
                            type="submit",
                            class_name="px-4 py-2 bg-blue-500 text-white rounded",
                        ),
                        class_name="flex justify-end",
                    ),
                    on_submit=TransactionFormState.add_transaction,
                ),
            ),
            class_name="bg-white p-6 rounded-lg shadow-lg w-1/3",
        ),
        class_name="fixed inset-0 open:flex items-center justify-center bg-black bg-opacity-50 z-50",
        open=TransactionFormState.show_dialog,
    )