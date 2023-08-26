from unittest.mock import patch
from psycopg2 import OperationalError as psycopg2OpError
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase
import time

class CommandTest(SimpleTestCase):
    """Test commands"""

    @patch('user.management.commands.wait_for_db.Command.check')
    def test_wait_for_db_ready(self, patched_check):
        """Testing waiting for database if the database is ready"""
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])

    @patch.object(time, 'sleep')
    @patch('user.management.commands.wait_for_db.Command.check')
    def test_wait_for_db_delay(self, patched_check, patched_sleep):
        """Testing for the database when getting operational error"""
        patched_check.side_effect = [psycopg2OpError] * 2 + \
                                    [OperationalError] * 3 + [True]
        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])

# This is an empty line at the end of the file.
