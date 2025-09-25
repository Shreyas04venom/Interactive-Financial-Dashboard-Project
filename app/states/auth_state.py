import reflex as rx


class AuthState(rx.State):
    users: dict[str, str] = {"admin@reflex.com": "password123"}
    in_session: bool = True
    user_email: str = "admin@reflex.com"

    @rx.event
    def sign_up(self, form_data: dict[str, str]):
        if form_data["email"] in self.users:
            yield rx.toast.error("Email already in use")
        else:
            self.users[form_data["email"]] = form_data["password"]
            self.in_session = True
            self.user_email = form_data["email"]
            return rx.redirect("/")

    @rx.event
    def sign_in(self, form_data: dict[str, str]):
        if (
            form_data["email"] in self.users
            and self.users[form_data["email"]] == form_data["password"]
        ):
            self.in_session = True
            self.user_email = form_data["email"]
            return rx.redirect("/")
        else:
            self.in_session = False
            yield rx.toast.error("Invalid email or password")

    @rx.event
    def sign_out(self):
        self.in_session = False
        self.user_email = ""
        return rx.redirect("/sign-in")

    @rx.event
    def check_session(self):
        if not self.in_session:
            return rx.redirect("/sign-in")