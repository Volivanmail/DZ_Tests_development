import requests

def token_yadi():
    with open('D:\\Study_Pyton\\dip_par\\token_YaDi.txt', encoding='utf-8') as f:
        token_yadi = f.read().strip()
        return token_yadi

def add_folder(path):
    token = token_yadi()
    url = 'https://cloud-api.yandex.net/v1/disk/resources?path=' + path
    headers = {'Accept': 'application/json', 'Authorization': 'OAuth ' + token}
    r = requests.put(url, headers=headers)
    return r.status_code

if __name__ == '__main__':
    add_folder()


