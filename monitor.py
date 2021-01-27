import requests 
import logging
from plyer import notification

logging.basicConfig(
    filename='logs',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'icon.ico',
        timeout = 10,
    )

def check_status():
    try:
        # insert your url here
        url = 'https://github.com/neoScriptscode/someRandomRepo'
        req = requests.get(url)
        print(req.status_code)

        if (req.status_code != 200): 
            msg = f'{url} is down'
            logging.info(msg)
            print(msg)
            notify('Oh no', msg)
        else: 
            msg = f'Everything is ok {url} is up...'
            logging.info(msg)
            print(msg)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    check_status()