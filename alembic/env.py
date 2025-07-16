from logging.config import fileConfig
import os
from dotenv import load_dotenv

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# 🌱 Load .env variables (like DATABASE_URL)
load_dotenv()

# ⚙️ Alembic configuration object
config = context.config

# 🗂️ Set SQLAlchemy URL from .env
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

# 📝 Logging setup (optional but good)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 🔧 Target metadata for autogenerate
from app.models import Base
target_metadata = Base.metadata

# 🔁 Offline Migrations
def run_migrations_offline() -> None:
    """Run migrations without a live DB connection."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# 🔁 Online Migrations
def run_migrations_online() -> None:
    """Run migrations with a live DB connection."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

# 🚀 Choose migration mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()




