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
    
def public_data(value):
    """Remove common contact fields before passing evidence to the model"""
    if isinstance(value, dict):
        return {k: public_data(v) for k,v in value.items if not any(s in k.lower() for s in ('email', 'phone', 'mobile', 'address', 'contact', 'password', 'token'))}
    
    if isinstance(value, list):
        return [public_data(v) for v in value[:15]]
    
    if isinstance(value, str):
        return re.sub(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', '[redacted]', value)[:10000]
    return value

