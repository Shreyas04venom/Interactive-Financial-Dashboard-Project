import reflex as rx
from app.states.state import State, TransactionData
from typing import cast


class TransactionFormState(rx.State):
    show_dialog: bool = False

    def open_dialog(self):
        self.show_dialog = True

    def close_dialog(self):
        self.show_dialog = False

    @rx.event
    async def add_transaction(self, form_data: dict):
        main_state = await self.get_state(State)
        amount = float(form_data["amount"])
        transaction_type = form_data["type"]
        if transaction_type == "expense":
            amount = -abs(amount)
        new_transaction = cast(
            TransactionData,
            {
                "date": form_data["date"],
                "description": form_data["description"],
                "amount": amount,
                "type": transaction_type,
            },
        )
        main_state.transactions_data.insert(0, new_transaction)
        self.show_dialog = False