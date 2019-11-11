from django.conf import settings
from django.http import HttpResponse
from django.conf.urls import url
from django.views.decorators.http import require_POST  # 目前的 API 视图只能用于接收 POST 请求
from django.http import JsonResponse  # 用于返回 JSON 数据
import subprocess
from django.views.decorators.csrf import csrf_exempt


setting = {'DEBUG': True, 'ROOT_URLCONF': __name__}
settings.configure(**setting)  # 配置基本设置，另一种方法时Django.setup()


def home(request):  # 视图函数，返回一个字符串
    with open('index.html', 'rb') as f:  # 'rb'表示以二进制打开，结果时r''形式的字节串，以免夹杂未知语言
        html = f.read()
    return HttpResponse(html)


def run_code(code):
    try:
        output = subprocess.check_output(['python', '-c', code],
                                         universal_newlines=True,
                                         stderr=subprocess.STDOUT,
                                         timeout=10)
        # 在python脚本中执行python字符串，universal_newlines的设置将返回的字节串转为字符串,
        # strderr的设置在子进程报错时会返回错误信息, timeout超时会直接报错
    except subprocess.CalledProcessError as e:
        output = e.output
    except subprocess.TimeoutExpired as t:
        output = '\r\n'.join('time out', t.output)

    return output


@csrf_exempt  # 不使用表单时需要禁用csrf功能
@require_POST
def api(request):
    code = request.POST.get('code')
    output = run_code(code)
    return JsonResponse(data={'output': output})


urlpatterns = [url('^api/$', api, name='api'), url('^$', home, name='home')]

if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
