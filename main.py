import requests

url = "https://api.telegram.org/bot73349262:AAGQEevFjZmiF0tWyPJPwGP3A_7DjdzyhmY/"

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


response = requests.get('https://api.telegram.org/bot73349262:AAGQEevFjZmiF0tWyPJPwGP3A_7DjdzyhmY/getUpdates')
print(response)
