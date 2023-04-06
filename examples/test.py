import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = 'text=Hello%20from%20Python!&x=0&y=13&r=255&g=255&b=255&identifier=0&font=1&width=64&movement_speed=20&direction=0'

response = requests.post('http://localhost:8086/sendText', headers=headers, data=data)