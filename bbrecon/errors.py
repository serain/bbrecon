import json


class ApiResponseError(Exception):
    def __init__(self, *, code: int, detail: str):
        super().__init__()
        self.code: int = code
        self.detail: str = detail

    def to_dict(self) -> dict:
        return {"code": self.code, "detail": self.detail}

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
