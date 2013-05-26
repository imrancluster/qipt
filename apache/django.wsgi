import os, sys

path = '/home/imran/PycharmProjects/qipt'
if  path  not in sys.path:
    sys.path.insert(0, '/home/imran/PycharmProjects/qipt')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qipt.settings')

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
