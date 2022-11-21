from typing import Optional

from pydantic import BaseModel


class ScanProfile(BaseModel):
    level: int
    reference: str
    scan_profile_type: Optional[str]
