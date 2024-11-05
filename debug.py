import sys,os,platform
import crysisconfig as cfg
# В РАЗРАБОТКЕ
def debug():
    print("-_-_- РЕЖИМ ОТЛАДКИ -_-_-")
    print("Версия cparser: " + cfg.version)
    system = platform.system()
    if system == "Linux":
        linux_info = platform.freedesktop_os_release()
        print(linux_info)
    p_version = platform.python_version()
    print("Операционная система:" + system)
    print("Версия PYTHON:" + p_version)
    print("-_-_- РЕЖИМ ОТЛАДКИ -_-_-")
