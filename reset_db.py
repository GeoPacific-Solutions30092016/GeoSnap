import asyncio
from app.db import engine
from app.models import Base
import app.models.user  # 👈 ensures User is loaded

async def reset_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(reset_db())
