import requests 
import logging


logging.basicConfig(
    filename='logs',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def check_status():
    try:
        url = 'https://github.com'
        req = requests.get(url)
        print(req.status_code)

        if (req.status_code != 200): 
            msg = f'{url} is down'
            logging.info(msg)
            print(msg)
        else: 
            msg = f'Everything is ok {url} is up...'
            logging.info(msg)
            print(msg)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    check_status()