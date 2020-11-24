from celery import shared_task
from django.core.management import call_command


@shared_task
def backup():
    call_command('dbbackup', '--clean')
    call_command('mediabackup', '--clean')
