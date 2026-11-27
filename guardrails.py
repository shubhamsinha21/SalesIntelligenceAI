import re
from urllib.parse import urlsplit

def valid_company(name):
    name = name.strip()
    if not 2 <= len(name) <=100 or not re.fullmatch(r"[\w .,&'()\-+]+", name):
        raise ValueError('Enter a company name (2-100 characters).')
    
    return name

def safe_url(url):
    try:
        p = urlsplit(url)
        host = p.hostname or ''
        return p.schema == 'https' and '.' in host and not p.username and not p.password and not re.fullmatch(r'[\d.]+', host) and not host.endswith(('.local', '.internal', '.localhost')) and p.port in (None, 443)
    except (ValueError, TypeError):
        return False
    


