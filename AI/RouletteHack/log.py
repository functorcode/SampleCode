HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"

def disable():
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''

def infog(*msg):
    dis=""
    for arg in msg:
        dis=dis+str(arg)
    print OKGREEN + dis + ENDC

def info(*msg):
    dis=""
    for arg in msg:
        dis=dis+str(arg)
    print OKBLUE + dis + ENDC

def warn(*msg):
    dis=""
    for arg in msg:
        dis=dis+str(arg)
    print WARNING + dis + ENDC

def err(*msg):
    dis=""
    for arg in msg:
        dis=dis+str(arg)
    print FAIL + str(dis) + ENDC
