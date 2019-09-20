import time


def log(*args, **kwargs):
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


def log_nfa(pair_out):
    log('from: ', pair_out.start_node.status_num, 'to: ',
        pair_out.end_node.status_num, 'in: ', pair_out.start_node.edge)
    if hasattr(pair_out.start_node, 'input_set'):
        log('input set: ', pair_out.start_node.input_set)    