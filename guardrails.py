import re
from urllib.parse import urlparse

def valid_company(name):
    name = name.strip()
    if not 2 <= len(name) <=100 or not re.fullmatch(r"[\w .,&'()\-+]+", name):
        raise ValueError('Enter a company name (2-100 characters).')
    
    return name

