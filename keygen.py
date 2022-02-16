import hashlib
import time
import base64
import random
import uuid

# To generate license key with format XXXX-XXXX-XXXX-XXXX

salt = "THIS_IS_YOUR_SALT_USE_RANDOM_STRING"
print("Licence key generator")
# UUID format is always UUID('ae66f1f5-ec93-4f42-a757-b8f5b939ae7e')
random_user_id = str(uuid.uuid4()).split('-')[1] # so the length of this string will always be 4

# base 64 encoding of user_id & 
hash_user_id = hashlib.sha256(random_user_id.encode()).hexdigest()[:12] # Get first 12 chars of hash string
license_key = "{}-{}-{}-{}".format(
    hash_user_id[:4],
    hash_user_id[4:8],
    hash_user_id[8::],
    random_user_id
).upper()

print("Your licence key: {}".format(license_key))