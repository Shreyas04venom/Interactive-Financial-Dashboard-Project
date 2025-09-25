import reflex as rx
from app.states.transaction_form_state import TransactionFormState


def add_transaction_modal() -> rx.Component:
    return rx.el.dialog(
        rx.el.div(
            class_name="fixed inset-0 bg-black bg-opacity-50 backdrop-blur-sm",
            on_click=TransactionFormState.close_dialog,
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Add Transaction", class_name="text-2xl font-bold text-gray-900"
                ),
                rx.el.p(
                    "Fill in the details below to add a new transaction.",
                    class_name="text-sm text-gray-600 mb-6",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Date", class_name="text-sm font-medium text-gray-700"
                        ),
                        rx.el.input(
                            name="date",
                            type="date",
                            required=True,
                            class_name="w-full mt-1 p-2 border border-gray-300 rounded-lg shadow-sm",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Description",
                            class_name="text-sm font-medium text-gray-700",
                        ),
                        rx.el.input(
                            name="description",
                            required=True,
                            class_name="w-full mt-1 p-2 border border-gray-300 rounded-lg shadow-sm",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Amount", class_name="text-sm font-medium text-gray-700"
                        ),
                        rx.el.input(
                            name="amount",
                            type="number",
                            step="0.01",
                            required=True,
                            class_name="w-full mt-1 p-2 border border-gray-300 rounded-lg shadow-sm",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Type", class_name="text-sm font-medium text-gray-700"
                        ),
                        rx.el.select(
                            rx.el.option("Income", value="income"),
                            rx.el.option("Expense", value="expense"),
                            rx.el.option("Investment", value="investment"),
                            name="type",
                            required=True,
                            class_name="w-full mt-1 p-2 border border-gray-300 rounded-lg shadow-sm",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Cancel",
                            type="button",
                            on_click=TransactionFormState.close_dialog,
                            class_name="mr-2 px-4 py-2 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300",
                        ),
                        rx.el.button(
                            "Add Transaction",
                            type="submit",
                            class_name="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700",
                        ),
                        class_name="flex justify-end pt-4 border-t border-gray-200",
                    ),
                    on_submit=TransactionFormState.add_transaction,
                    reset_on_submit=True,
                ),
                class_name="bg-white p-8 rounded-xl shadow-lg w-full max-w-md",
            ),
            class_name="z-50",
        ),
        class_name="fixed inset-0 open:flex items-center justify-center bg-black bg-opacity-50 z-50",
        open=TransactionFormState.show_dialog,
    )