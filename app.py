import hashlib

salt = "THIS_IS_YOUR_SALT_USE_RANDOM_STRING"
key = input("Please enter you licence key: ")

if len(key.split("-")) != 4:
    print("Wrong licence key format, abort.")
    exit(-1)

random_user_id = key.split("-")[3].lower()

hash_user_id = hashlib.sha256(random_user_id.encode()).hexdigest()[:12] # Get first 12 chars of hash string
# Generate the license key with same salt and same algo, then check the result 
generate_license_key = "{}-{}-{}-{}".format(
    hash_user_id[:4],
    hash_user_id[4:8],
    hash_user_id[8::],
    random_user_id
).upper()

print(generate_license_key)

if generate_license_key == key:
    print("Valid license key, pass")
else:
    print("Invalid license key, failed")
