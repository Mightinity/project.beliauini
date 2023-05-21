import socket
import time
import requests

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error:
        return "Gagal mendapatkan IP Address"

def get_ngrok():
    headers = {
        'Authorization': 'Bearer 2PxtULMOFp62JnqZsvktUe5blBy_7fQDaaupEBpZF2tKtTXM3',
        'Ngrok-Version': '2'
    }
    response = requests.get('https://api.ngrok.com/tunnels', headers=headers)
    if response.status_code == 200:
        tunnels = response.json()['tunnels']
        if(len(tunnels) == 0):
            time.sleep(2)
            return get_ngrok()
        else:            
            ip, port = "".join([tunnel['public_url'] for tunnel in tunnels]).removeprefix("tcp://").split(":")
            return ip, port
    else:
        return "gagal", "dapat"

