# Copyright 2017 DM1881 AS.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
