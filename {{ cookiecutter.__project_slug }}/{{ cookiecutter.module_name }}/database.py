import configparser
import logging

from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine


@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, _):
    """Emit PRAGMA statement automatically for all new connections.

    See https://docs.sqlalchemy.org/en/20/dialects/sqlite.html#foreign-key-support
    """
    ac_setting = dbapi_connection.autocommit
    dbapi_connection.autocommit = True

    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

    dbapi_connection.autocommit = ac_setting


def get_db(settings_filepath):
    """Provide a SQLAlchemy engine from the given database settings."""
    config = configparser.ConfigParser()
    config.read(settings_filepath)
    db_filename = config.get("Database", "SqliteFile")
    log_level = config.get("Database", "LogLevel")

    logging.getLogger("sqlalchemy.engine").setLevel(log_level)
    return create_engine(f"sqlite:///{db_filename}", connect_args={"autocommit": False})
