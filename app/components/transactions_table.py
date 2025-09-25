import reflex as rx
from app.states.state import State


def transaction_row(transaction: rx.Var) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            transaction["date"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        rx.el.td(
            transaction["description"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-900",
        ),
        rx.el.td(
            rx.text(
                rx.cond(
                    transaction["amount"] > 0,
                    f"+${transaction['amount'].to_string()}",
                    f"-${str(abs(transaction['amount']))}",
                ),
                class_name=rx.cond(
                    transaction["amount"] > 0, "text-green-600", "text-red-600"
                ),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium",
        ),
        rx.el.td(
            rx.el.span(
                transaction["type"],
                class_name=rx.cond(
                    transaction["type"] == "income",
                    "bg-green-100 text-green-800",
                    rx.cond(
                        transaction["type"] == "expense",
                        "bg-red-100 text-red-800",
                        "bg-blue-100 text-blue-800",
                    ),
                )
                + " px-2 inline-flex text-xs leading-5 font-semibold rounded-full",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
    )


def transactions_table() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Recent Transactions", class_name="text-lg font-semibold text-gray-900 mb-4"
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Date",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Description",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Amount",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Type",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                    )
                ),
                rx.el.tbody(
                    rx.foreach(State.transactions_data, transaction_row),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg",
        ),
        class_name="bg-white p-6 rounded-lg shadow",
    )