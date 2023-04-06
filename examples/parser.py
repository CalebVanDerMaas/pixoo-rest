#init main python script
import sys
import os
import json
import requests
import time

def main():
    def parse(data):
        str(data)
        data_dict = json.loads(data)
        answer = []
        for i, item in enumerate(data_dict['results']):
            answer.append(item['properties']['Task']['title'][0]['text']['content'])
        return answer
            
    parsed_data = parse(sys.argv[1])

    headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
    }

    files = {
        'gif': open('/Users/calebvandermaas/Developer/Pixoo64Dev/pixoo-rest/examples/BlackBackground.png', 'rb'),
        'speed': (None, '100'),
    }

    response = requests.post('http://localhost:8086/sendGif', headers=headers, files=files)

    #clear HTTP text
    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    }

    json_data = {
    'Command': 'Draw/ClearHttpText',
    }

    response = requests.post('http://localhost:8086/passthrough/draw/clearHttpText', headers=headers, json=json_data)

    print(parsed_data)
    print(parsed_data[0])

    #send text to HTTP
    for i,data in enumerate(parsed_data):
        identifier = i + 1
        position = i * 12

        formatted_data = data.replace(' ', '%20')

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = f'text={"-%20" + formatted_data}&x=0&y={position}&r=255&g=255&b=255&identifier={identifier}&font=2&width=64&movement_speed=30&direction=0'
        response = requests.post('http://localhost:8086/sendText', headers=headers, data=data)

    time.sleep(25)

    headers = {
        'accept': 'application/json',
    }

    response = requests.put('http://localhost:8086/channel/0', headers=headers)

if __name__ == "__main__":
    main()
