# osumodel
使用 pydantic 與 httpx 使 Python 有 Typing 的 OsuAPI 工具

目前僅支持v1

# setup
```
pip install pydantic httpx
```

# 使用方法
首先在資料夾下建立.env檔案
```
APIMODEL_API_KEY=
APIMODEL_CLIENT_ID=
APIMODEL_CLIENT_SECRET=
APIMODEL_CLIENT_REDIRECT_URL=
```

.py
```py
import asyncio
from osumodel import v1

async def main():
    u = await v1.User.get(u=840)
    print(u)

if __name__ == "__main__":
    asyncio.run(main)
```
