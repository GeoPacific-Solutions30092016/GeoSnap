from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# 🌱 Load environment variables from .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# 🚀 Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# 📚 Define base class for models
Base = declarative_base()

# 🗂️ Create async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 🧼 Graceful engine shutdown (optional for FastAPI lifespan events)
async def shutdown():
    await engine.dispose()

# 📦 Dependency for route-level DB sessions
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


