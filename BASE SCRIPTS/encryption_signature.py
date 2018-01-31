#  Created by Bogdan Trif on 29-01-2018 , 1:32 PM.
api_key = '6cb3dde7be1f42f980a11f5dab414b7f'
api_secret = '6acd9f768ae947c6899fb471fb2b269c'

import hashlib
import hmac
import base64


def make_digest(message, key):

    key = bytes(key, 'UTF-8')
    message = bytes(message, 'UTF-8')

    digester = hmac.new(key, message, hashlib.sha512)
    print(digester)
#     signature1 = digester.hexdigest()
    signature1 = digester.digest()

    print(signature1)

    #signature2 = base64.urlsafe_b64encode(bytes(signature1, 'UTF-8'))
    signature2 = base64.urlsafe_b64encode(signature1)
    print(signature2)

    return str(signature2, 'UTF-8')


result = make_digest('Ce frumos este primavara !', api_secret)
print(result)

print('\n api_key, api_secret : ')
print(make_digest(api_key, api_secret))


