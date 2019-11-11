import subprocess


def run_cdoe(code):
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


code = """print('Test success')"""
print(run_cdoe(code))
