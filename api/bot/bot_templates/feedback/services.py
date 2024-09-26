import requests


def send_message(msg, name, chat_id, bot_token):
    data = {
        'message': msg,
        'user_name': name,
        'chat_id': chat_id,
        'bot_token': bot_token
    }
    r = requests.post("http://127.0.0.1:8000/tg-bot-api/message/", data=data)

    if r.ok:
        return True
    return False
