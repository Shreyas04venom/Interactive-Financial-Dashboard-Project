import reflex as rx
from app.states.state import State


def net_worth_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Net Worth", class_name="text-lg font-semibold text-gray-900 mb-4"),
        rx.recharts.line_chart(
            rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
            rx.recharts.x_axis(data_key="month"),
            rx.recharts.y_axis(),
            rx.recharts.tooltip(),
            rx.recharts.line(data_key="value", stroke="#8884d8", active_dot={"r": 8}),
            data=State.net_worth_data,
            width=500,
            height=300,
        ),
        class_name="bg-white p-6 rounded-lg shadow",
    )