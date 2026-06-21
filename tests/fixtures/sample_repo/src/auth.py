class SessionManager:
    def create_session(self, user_id: str) -> str:
        return f"session:{user_id}"

    def validate_session(self, token: str) -> bool:
        return token.startswith("session:")


def login(username: str, password: str) -> bool:
    return username == "admin" and password == "secret"
