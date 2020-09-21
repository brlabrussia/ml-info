from django.core.management import call_command
from django.utils.timezone import localtime

from celery import shared_task


@shared_task
def backup():
    filedir = '/usr/src/app/fixtures/'
    filename = f'{localtime().date().isoformat()}.json'
    filepath = filedir + filename
    call_command(
        'dumpdata',
        '--natural-foreign',
        '-e', 'admin',
        '-e', 'contenttypes',
        '-e', 'auth.Permission',
        '--indent', '4',
        '-o', filepath,
    )
