from django.conf import settings
from django.http import HttpResponse
from django.conf.urls import url

setting = {'DEBUG': True, 'ROOT_URLCONF': __name__}
settings.configure(**setting)  # 配置基本设置，另一种方法时Django.setup()


def home(request):  # 视图函数，返回一个字符串
    return HttpResponse('hello world')


urlpatterns = [url('^$', home, name='home')]

if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
