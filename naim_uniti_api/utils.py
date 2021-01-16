
def get_current_value(base_url, url_path, value):
    req = requests.get(base_url + url_path)
    if r.status_code == 200:
        content = r.content
        if type(content) == bytes:
            content = content.decode()
        j = json.loads(r.content)
        if variable in j:
            return j[variable]

def put_new_value(base_url, url_path, data):
    return requests.put(base_url + url_path, data=data)
