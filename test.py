import requests

def check_internet():
    ''' checar conexão de internet '''
    url = 'https://www.google.com'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except:
        return False

if not check_internet():
    print('Internet fora do ar!')
else:
    print('Internet OK!')