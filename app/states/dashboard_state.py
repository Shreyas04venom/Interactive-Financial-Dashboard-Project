import reflex as rx


class DashboardState(rx.State):
    @rx.var
    def active_page(self) -> str:
        return self.router.page.path.strip("/") or "dashboard"