from dataclasses import dataclass
from typing import Dict


@dataclass
class Client:
    base_url: str

    def get_headers(self) -> Dict[str, str]:
        return {}


@dataclass
class AuthenticatedClient(Client):
    token: str

    def get_headers(self) -> Dict[str, str]:
        return {"X-API-KEY": self.token}
