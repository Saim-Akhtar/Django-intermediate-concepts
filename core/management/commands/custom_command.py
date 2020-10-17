from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('username',type=str)

    def handle(self,*args,**options):
        username = options['username']
        self.stdout.write(self.style.SUCCESS(f'We called username {username}'))