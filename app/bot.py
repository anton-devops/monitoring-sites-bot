import requests
from time import sleep
from os import environ as env
from dotenv import load_dotenv


def send_to_telegram(message):
    apiToken = env.get('API_TOKEN')
    chatID = env.get('CHAT_ID')
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)


def main():
    load_dotenv()
    DELAY = int(env.get('DELAY'))
    URLs = {url: {'status': True} for url in [url for url in env.get("URLS").split(" ")] if url}

    while True:
        for url, status in URLs.items():
            try:
                response = requests.get(f'https://{url}', timeout=DELAY)
                if not response.ok and status["status"]:
                    send_to_telegram(f'WARNING: сайт https://{url} перестал работать!')
                    print(f'WARNING: {url} is down!')
                    status["status"] = False
                if response.ok and not status["status"]:
                    send_to_telegram(f'INFO: сайт https://{url} снова работает!')
                    print(f'INFO: https://{url} is UP!')
                    status["status"] = True
            except:
                if status["status"]:
                    send_to_telegram(f'WARNING: сайт https://{url} слишком долго не открывается!')
                    print(f'WARNING: https://{url} TIMEOUT!')
                status["status"] = False
            # print(f'{url} -> {status["status"]}')
        sleep(DELAY)


if __name__ == '__main__':
    main()
