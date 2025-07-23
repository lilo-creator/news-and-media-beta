from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Create the UserProfile table manually'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS accounts_userprofile (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    profile_picture VARCHAR(100),
                    phone_number VARCHAR(15) NOT NULL,
                    date_of_birth DATE,
                    gender VARCHAR(1) NOT NULL,
                    bio TEXT NOT NULL,
                    location VARCHAR(100) NOT NULL,
                    website VARCHAR(200) NOT NULL,
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    user_id INTEGER NOT NULL UNIQUE REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED
                );
            """)
            
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS accounts_userprofile_user_id_62e0e68a 
                ON accounts_userprofile (user_id);
            """)
            
            self.stdout.write(
                self.style.SUCCESS('Successfully created accounts_userprofile table')
            )
