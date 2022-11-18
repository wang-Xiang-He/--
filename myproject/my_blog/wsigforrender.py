import os
import sys

path = '/myproject'  #修改成 `/home/pythonanywhere帳號/Django Project名稱`
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'my_blog.settings' #修改成 'Django Project名稱.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
