"""Django command to wait for the database to be available"""

from typing import Any, Optional
from psycopg2 import OperationalError as psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
import time


class Command(BaseCommand):
    """django command for waiting db"""
    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write("waiting for database")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2OpError, OperationalError):
                self.stdout.write("database is unavailable")
                time.sleep(1)
        self.stdout.write("Database is available")

# This is an empty line at the end of the file.
