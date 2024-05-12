import unittest
from unittest.mock import MagicMock

from security.authentication import Authentication


class TestAuthentication(unittest.TestCase):
    def setUp(self):
        self.authenticator = Authentication("test.db")
        self.authenticator.db = MagicMock()
        self.cursor = MagicMock()
        self.authenticator.db.cursor = self.cursor

    def test_authenticate_user_valid_credentials(self):
        self.cursor.fetchone.return_value = ("hashed_password", "role")
        role = self.authenticator.authenticate_user("username", "password", "role")
        self.assertEqual(role, "role")

    def test_authenticate_user_invalid_credentials(self):
        self.cursor.fetchone.return_value = None
        role = self.authenticator.authenticate_user("username", "password", "role")
        self.assertIsNone(role)


if __name__ == '__main__':
    unittest.main()
