import time


class G:
    dfa_list = []
    group_list = []
    on_partition = True


def log(*args, **kwargs):
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


def list_dict(width):
    return [dict() for i in range(width)]
