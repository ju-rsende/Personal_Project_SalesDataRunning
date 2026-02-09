from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management.utils import get_random_secret_key
import getpass

class Command(BaseCommand):
    help = 'Set admin password securely'

    def handle(self, *args, **options):
        try:
            admin = User.objects.get(username='admin')
            password = getpass.getpass('Enter new admin password: ')
            if not password:
                password = get_random_secret_key()[:12]
                self.stdout.write(f'Generated password: {password}')
            
            admin.set_password(password)
            admin.save()
            self.stdout.write('Password updated successfully')
            
        except User.DoesNotExist:
            self.stdout.write('Admin user not found')