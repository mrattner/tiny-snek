import configparser
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.event import listen
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read("settings.ini")

def set_sqlite_pragma(dbapi_connection, connection_record):
    """Enable the checking of foreign key constraints on a SQLite connection."""
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

class Database:
    engine = None
    create_session = None

    @classmethod
    def init(cls, environment="DEFAULT", echo=False):
        """Provides a SQLAlchemy engine for the database in the given environment.
        """
        dialect = config.get(environment, "dialect")
        driver = config.get(environment, "driver")
        username = config.get(environment, "username")
        password = config.get(environment, "password")
        host = config.get(environment, "hostname")
        port = config.get(environment, "port")
        database = config.get(environment, "database")

        url = "{dialect}{driver}://{username}{password}{host}{port}/{database}"\
            .format(dialect=dialect,
                driver=("+" + driver if driver else ""),
                username=username,
                password=(":" + password if password else ""),
                host=("@" + host if host else ""),
                port=(":" + port if port else ""),
                database=database)

        Database.engine = create_engine(url, echo=echo)
        Database.create_session = sessionmaker(bind=Database.engine)

        if dialect == "sqlite":
            listen(Engine, "connect", set_sqlite_pragma)

    @classmethod
    @contextmanager
    def session_scope(cls):
        """Provide a transactional scope around a series of operations.
        See http://docs.sqlalchemy.org/en/rel_1_1/orm/session_basics.html
        """
        if not Database.create_session:
            raise RuntimeError("Must initialize engine before creating session")

        session = Database.create_session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

