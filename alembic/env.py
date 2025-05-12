from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from mymodel import Base  # Asegúrate de importar tu modelo base aquí

# Esta es la configuración de Alembic, que proporciona
# acceso a los valores dentro del archivo .ini que estamos usando.
config = context.config

# Interpretar el archivo de configuración para la configuración de logging.
if config.config_file_name:
    fileConfig(config.config_file_name)

# Definir la metadata del modelo para soportar 'autogenerate' si es necesario
target_metadata = Base.metadata  # Cambié de None a Base.metadata, ajusta según tu estructura

def run_migrations_offline() -> None:
    """Ejecutar migraciones en modo 'offline'.

    En este modo solo configuramos la URL de la base de datos, sin necesidad de un Engine.
    Las consultas a context.execute() aquí emiten las migraciones en el script de salida.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecutar migraciones en modo 'online'.

    En este escenario necesitamos crear un Engine y asociar una conexión con el contexto.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


# Ejecutar según el modo de conexión (offline u online)
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
