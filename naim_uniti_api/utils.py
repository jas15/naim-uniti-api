
def get_current_value(base_url, url_path, value=None, params=None):
    req = requests.get(base_url + url_path, params=params)
    if r.status_code == 200:
        content = r.content
        if type(content) == bytes:
            content = content.decode()
        j = json.loads(r.content)
        if value is not None and value in j:
            return j[value]

def put_new_value(base_url, url_path, data):
    return requests.put(base_url + url_path, data=data)
