
import time
from get_xgb import get_xgb
from get_cls import get_cailianshe

def run():
    get_xgb()
    get_cailianshe()



if __name__ == '__main__':
    while True:
        run()
        time.sleep(30)
