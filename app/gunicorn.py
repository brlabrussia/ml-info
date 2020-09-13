import os
from multiprocessing import cpu_count

bind = '0.0.0.0:8080'
max_requests = 1000
timeout = 300

worker_class = 'gevent'
workers = int(os.getenv('WORKERS', cpu_count()))

if bool(os.getenv('DEBUG', False)):
    reload = True
