import io
import unittest
from contextlib import contextmanager

from sqlalchemy import func, insert, select

import {{ cookiecutter.module_name }}.models as m
from {{ cookiecutter.module_name }}.database import get_db


class DbIntegrationTest(unittest.TestCase):
    """Initializes in-memory SQLite engine and wraps each test in a connection with a transaction."""

    @classmethod
    def setUpClass(cls):
        cls.engine = get_db(io.StringIO(""))
        m.init_schema(cls.engine)

    @classmethod
    def tearDownClass(cls):
        cls.engine.dispose()

    @contextmanager
    def isolated_txn(self):
        conn = self.engine.connect()
        try:
            yield conn
        finally:
            conn.rollback()

    def setUp(self):
        self.conn = self.enterContext(self.isolated_txn())


class TestFoo(DbIntegrationTest):
    def test_insert_org(self):
        insert_stmt = insert(m.organization).values(name="FlortCo", prefix="3f0d")
        self.conn.execute(insert_stmt)

        count_stmt = select(func.count()).select_from(m.organization)
        count = self.conn.scalar(count_stmt)
        self.assertEqual(count, 1)

        query = select(m.organization).where(m.organization.c.name == "FlortCo")
        result = self.conn.execute(query)
        row = result.one()
        self.assertEqual(row.prefix, "3f0d")

    def test_insert_users(self):
        insert_stmt = insert(m.user).values(
            [
                {"name": "SpongeBob Squarepants", "email": "spongebob@flort.co"},
                {"name": "Sandy Cheeks", "email": "sandy@flort.co"},
                {"name": "Patrick Star", "email": "patrick@flort.co"},
            ]
        )
        self.conn.execute(insert_stmt)

        count_stmt = select(func.count()).select_from(m.user)
        count = self.conn.scalar(count_stmt)
        self.assertEqual(count, 3)

        query = select(m.user).where(m.user.c.email == "patrick@flort.co")
        result = self.conn.execute(query)
        row = result.one()
        self.assertEqual(row.name, "Patrick Star")
