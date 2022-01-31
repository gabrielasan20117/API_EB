import requests

def API_Title():
    url = 'https://api.stagingeb.com/v1/properties?page=1&limit=20&search%5Bstatuses%5D%5B%5D='
    api_key = {'X-Authorization': 'l7u502p8v46ba3ppgvj5y2aad50lb9'}
    req = requests.get(url,headers=api_key)
    if req.status_code == 200:
        response_json = req.json()
        content = response_json['content']
        listTitle = []
        for a in content:
            listTitle.append(a['title'])
        return print(listTitle)   
    if req.status_code == 400:
        response_json = req.json()
        error = response_json['error']
        return print(error)
    if req.status_code == 401:
        response_json = req.json()
        error = response_json['error']
        return print(error)
