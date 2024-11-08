import sys,os,platform
import cconfig as cfg
import pip._internal as pip
# В РАЗРАБОТКЕ
def debug():
    print("-_-_- РЕЖИМ ОТЛАДКИ -_-_-")
    print("Версия cparser: " + cfg.version)
    system = platform.system()
    if system == "Linux":
        linux_info = platform.freedesktop_os_release()
        print(linux_info)
    p_version = platform.python_version()
    compiler_version = platform.python_compiler()
    full_platform = platform.uname()
    print("Операционная система:" + system)
    print("Версия PYTHON:" + p_version)
    print(compiler_version)
    print(full_platform)


