import uuid
import base64
import boto3

from flask import current_app as app
from cryptography.fernet import Fernet
from pymemcache.client import base

from botocore import exceptions as botoexceptions


class IncogCrypto(object):
    def __init__(self):
        self.kms_key_id = app.config['KMS_KEY_ID']
        self.key_spec = 'AES_256'
        self.client = boto3.client('kms')

    def encrypt(self, data: str) -> dict:
        encrypted = {}
        try:
            response = self.client.generate_data_key(KeyId=self.kms_key_id, KeySpec=self.key_spec)
            key = base64.urlsafe_b64encode(response['Plaintext'])
            encrypted['key'] = base64.urlsafe_b64encode(response['CiphertextBlob'])

            f = Fernet(key)
            encrypted['value'] = f.encrypt(data.replace('\n', '\\n').encode('utf-8'))
        except (botoexceptions.ClientError, botoexceptions.EndpointConnectionError, TypeError) as error:
            raise error

        return encrypted

    def decrypt(self, cipher_text: dict) -> str:
        try:
            response = self.client.decrypt(CiphertextBlob=base64.urlsafe_b64decode(cipher_text['key']))

            f = Fernet(base64.urlsafe_b64encode(response['Plaintext']))
            clear_text = str(f.decrypt(cipher_text['value']).decode('utf-8'))
        except (botoexceptions.ClientError, botoexceptions.EndpointConnectionError, TypeError) as error:
            raise error

        return clear_text


class CacheStub(object):
    def __init__(self):
        cache_server = app.config['MEMCACHE_HOST']
        cache_port = app.config['MEMCACHE_PORT']
        self.expiration = app.config['MEMCACHE_SECRET_LIFESPAN']
        self.client = base.Client((cache_server, cache_port))

    def put_entry(self, key, val):
        return self.client.set(key=key, value=val, expire=self.expiration)

    def get_entry(self, key):
        return self.client.get(key=key)


class IncogWorkflow(object):
    def __init__(self):
        self.uuid = str(uuid.uuid1())

    def encrypt_user_data(self, value):
        enc_response = str(IncogCrypto().encrypt(value))
        CacheStub().put_entry(key=self.uuid, val=enc_response)
        return self.uuid

    @staticmethod
    def decrypt_user_data(key):
        enc_data = CacheStub().get_entry(key=key)
        if enc_data:
            return IncogCrypto().decrypt(eval(enc_data.decode()))
        else:
            return None
