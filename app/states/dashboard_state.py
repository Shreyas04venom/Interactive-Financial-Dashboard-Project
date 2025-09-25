import reflex as rx


class DashboardState(rx.State):
    active_page: str = "Dashboard"

    def set_active_page(self, page: str):
        self.active_page = page