def handle_qmake(x):
    if x[1] == 2000:
        return handle_x3(x)
    if x[1] == 1986:
        return handle_x0_qmake(x)


def handle_x3(x):
    if x[3] == 2001:
        return 0
    if x[3] == 2017:
        return 1
    return 2


def handle_x0_qmake(x):
    if x[0] == 1988:
        return 3
    if x[0] == 2020:
        return 4
    return 5


def handle_coq(x):
    if x[0] == 1988:
        return 6
    if x[0] == 1981:
        if x[1] == 2000:
            return 9
        return 8
    if x[0] == 2020:
        if x[1] == 2000:
            return 7
        return 8


def handle_x4(x):
    if x[4] == 'QMAKE':
        return handle_qmake(x)
    if x[4] == 'COQ':
        return handle_coq(x)
    if x[4] == 'TEXT':
        return 10
    return 10


def main(x):
    if x[2] == 1970:
        return 11
    if x[2] == 1959:
        return 12
    return handle_x4(x)
