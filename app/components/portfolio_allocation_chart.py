import reflex as rx
from app.states.state import State


def portfolio_allocation_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Portfolio Allocation",
            class_name="text-lg font-semibold text-gray-900 mb-4",
        ),
        rx.recharts.pie_chart(
            rx.recharts.pie(
                data_key="value",
                name_key="name",
                data=State.portfolio_data,
                cx="50%",
                cy="50%",
                outer_radius=80,
                fill="#8884d8",
                label=True,
            ),
            rx.recharts.tooltip(),
            width=500,
            height=300,
        ),
        class_name="bg-white p-6 rounded-lg shadow",
    )