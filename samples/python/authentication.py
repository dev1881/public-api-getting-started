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

import jwt
import datetime
from datetime import timedelta

def main():
    user = 'your user'
    secret = 'your secret'
    print generateToken(user, secret)

def unix_time_millis(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    return int((dt - epoch).total_seconds())


def generateToken(api_user=None, api_key=None, days=30):

    if api_user == None or api_key == None:
        print 'user and key needs to be set'

    user = api_user
    secret = api_key
    issuer = 'VK1881Issuer'
    audience = 'VK1881Services'

    today = datetime.datetime.today()
    next_30days = today + timedelta(days=days)

    expires = unix_time_millis(next_30days)
    now = unix_time_millis(datetime.datetime.utcnow())

    # This creates a token that is valid for 30 days.

    payload = {
        'VK1881Identity': user,
        'iss': issuer,
        'aud': audience,
        'exp': expires,
        'nbf': now
    }

    encoded = jwt.encode(payload, secret, algorithm='HS256')

    return encoded

if __name__ == '__main__':
    main()
