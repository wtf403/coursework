"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ


def max_workers():    
    return cpu_count()

command = '/home/std/coursework/backend/env/bin/gunicorn'
pythonpath = '/home/std/coursework/backend/'
workers = 3


bind = '127.0.0.1:' + environ.get('PORT', '8000')
max_requests = 1000
worker_class = 'gevent'
workers = max_workers()
