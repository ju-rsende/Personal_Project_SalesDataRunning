from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Set admin password'

    def handle(self, *args, **options):
        try:
            admin = User.objects.get(username='admin')
            admin.set_password('password')
            admin.save()
            self.stdout.write('Password set to: password')
        except User.DoesNotExist:
            self.stdout.write('Admin user not found')