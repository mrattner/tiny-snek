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


def get_db(settings_file):
    """Provide a SQLAlchemy engine from the given database settings."""
    config = configparser.ConfigParser()
    config.read_file(settings_file)
    # Empty string SQLite filename is the special in-memory database.
    db_filename = config.get("Database", "SqliteFile", fallback="")
    log_level = config.get("Database", "LogLevel", fallback="WARNING")

    logging.getLogger("sqlalchemy.engine").setLevel(log_level)
    return create_engine(f"sqlite:///{db_filename}", connect_args={"autocommit": False})
