import requests , os
from datetime import datetime
from config import CONFIG

def main():
    now = datetime.now()
    send_line_notify("テスtお"+str(now))

def send_line_notify(notification_message):
    line_notify_token = os.environ.get("ACCESS_TOKEN")
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message : {notification_message}'}
    requests.post(line_notify_api, headers= headers,data = data)

if __name__ == "__main__":
    main()
