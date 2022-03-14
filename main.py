from typing import List
from pydantic import BaseModel
from httpx import AsyncClient, Response
from settings import settings

class APIModel(BaseModel):
    __baseurl__: str = "https://osu.ppy.sh/api"
    __uri__: str = ""

    async def get(cls, **params):
        async with AsyncClient() as client:
            respone: Response = await client.get(
                url=cls.__baseurl__ + cls.__uri__,
                params=dict(**params, k=settings.api_key)
            )
            respone.raise_for_status()
            result: List[dict] = respone.json()
            data_length: int = len(result)
            if data_length == 0:
                return None
            if data_length > 1:
                return [cls(**r) for r in result]
            return cls(**result[0])
