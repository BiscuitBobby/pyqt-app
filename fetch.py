import requests

from api_key import api_key as key
def fetch(rover = 'curiosity',earth_date=''):
    if earth_date != '':
        x = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={earth_date}&api_key={key}'
    else:
        x = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos&api_key={key}'
    print('fetching url...')
    req = requests.get(x)
    content = (req.content)
    print(content)
    print(((str(content)[1::]).strip("'").strip('{}')))

d = fetch()
