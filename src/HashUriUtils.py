import re, base64

def get_hashuri_datapart(s):
    if not re.search(r'(.*[^A-Za-z0-9\-_]|)[A-Za-z0-9\-_]{25,}(\.[A-Za-z0-9\-_]{0,20})?', s):
        return ""
    return re.sub(r'^(.*[^A-Za-z0-9\-_]|)([A-Za-z0-9\-_]{25,})(\.[A-Za-z0-9\-_]{0,20})?$', r'\2', s)

def get_base64(s):
    return base64.b64encode(s, '-_')
