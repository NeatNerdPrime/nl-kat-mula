from typing import Optional

from scheduler.models import BoefjeMeta

from .services import HTTPService


class Bytes(HTTPService):
    name = "bytes"

    def __init__(self, host: str, source: str, user: str, password: str, timeout: int = 5):
        self.user: str = user
        self.password: str = password

        super().__init__(host=host, source=source, timeout=timeout)

        self.token = self._get_token(
            user=self.user,
            password=self.password,
        )

        self.headers.update({"Authorization": f"Bearer {self.token}"})

    def _get_token(self, user: str, password: str) -> str:
        url = f"{self.host}/token"
        response = self.post(
            url=url,
            payload={"username": user, "password": password},
            headers={"Content-Type": "application/x-www-form-urlendcoded"},
        )
        return str(response.json()["access_token"])

    def get_last_run_boefje(self, boefje_id: str, input_ooi: str) -> Optional[BoefjeMeta]:
        url = f"{self.host}/bytes/boefje_meta"
        response = self.get(
            url=url,
            params={
                "boefje_id": boefje_id,
                "input_ooi": input_ooi,
                "limit": 1,
                "descending": "true",
            },
        )
        if response.status_code == 200 and len(response.json()) > 0:
            return BoefjeMeta(**response.json()[0])  # FIXME: index

        return None
