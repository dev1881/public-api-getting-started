import requests

from authentication import generateToken


def main():
    client = 'your client account'
    user = 'your user'
    secret = 'your secret'
    token = generateToken(user, secret)

    url = 'https://api.1881.no/search/v1/unit'
    params = {
        'querystring': 'digitale medier 1881',
        # 'limit':'',
        # 'offset':'',
        'VK1881Client': client,
        'VK1881Token': token
    }
    response = requests.get(url, params)

    print 'Status code: %s' % response.status_code
    print response.content


if __name__ == '__main__':
    main()
