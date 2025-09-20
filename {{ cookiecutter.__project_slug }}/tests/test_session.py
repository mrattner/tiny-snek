import unittest

from {{ cookiecutter.module_name }}.database import Database as Db

class TestSession(unittest.TestCase):
    """Base class for a database integration test."""

    def setUp(self):
        """Connect to the test database and begin a wrapper transaction."""
        Db.init(environment="Test")
        self.connection = Db.engine.connect()
        self.transaction = self.connection.begin()

    def tearDown(self):
        """Rollback the wrapper transaction and close the connection."""
        self.transaction.rollback()
        self.connection.close()

class ExampleTest(TestSession):
    pass

