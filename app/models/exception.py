class CustomException(Exception):
    def __init__(self, http_code: int, message: str) -> None:
        self.http_code = http_code
        self.code = 0 if 200 <= http_code < 300 else 1
        self.message = message
        super().__init__(self.message)
